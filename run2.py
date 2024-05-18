import time
import torch
import numpy as np
from train_eval import train, init_network
from importlib import import_module

# 手动指定参数
model_name = 'TextRNN_Att'  # 模型选择: TextCNN, TextRNN, FastText, TextRCNN, TextRNN_Att, DPCNN, Transformer
embedding_choice = 'pre_trained'  # 是否使用预训练词向量: random 或 pre_trained
word_level = False  # 词级别或字符级别的处理: True 为词级别，False 为字符级别

if __name__ == '__main__':
    dataset = 'DETECTgpt'  # 数据集

    # 搜狗新闻:embedding_SougouNews.npz, 腾讯:embedding_Tencent.npz, 随机初始化:random
    embedding = 'detectGPT.npz' if embedding_choice == 'pre_trained' else 'random'
    if model_name == 'FastText':
        from utils_fasttext import build_dataset, build_iterator, get_time_dif
        embedding = 'random'
    else:
        from utils import build_dataset, build_iterator, get_time_dif

    x = import_module('models.' + model_name)
    config = x.Config(dataset, embedding)
    np.random.seed(1)
    torch.manual_seed(1)
    torch.cuda.manual_seed_all(1)
    torch.backends.cudnn.deterministic = True  # 保证每次结果一样

    start_time = time.time()
    print("Loading data...")
    vocab, train_data, dev_data, test_data = build_dataset(config, word_level)
    train_iter = build_iterator(train_data, config)
    dev_iter = build_iterator(dev_data, config)
    test_iter = build_iterator(test_data, config)
    time_dif = get_time_dif(start_time)
    print("Time usage:", time_dif)

    # train
    config.n_vocab = len(vocab)
    model = x.Model(config).to(config.device)
    if model_name != 'Transformer':
        init_network(model)
    print(model.parameters)
    train(config, model, train_iter, dev_iter, test_iter)
