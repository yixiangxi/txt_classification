import random

def split_dataset(input_txt, train_ratio=0.7, valid_ratio=0.2, test_ratio=0.1, shuffle=True):
    with open(input_txt, 'r', encoding='utf-8') as file:
        data = file.readlines()

    # 打乱数据
    if shuffle:
        random.shuffle(data)

    # 计算划分数量
    total_samples = len(data)
    train_samples = int(total_samples * train_ratio)
    valid_samples = int(total_samples * valid_ratio)
    test_samples = total_samples - train_samples - valid_samples

    # 划分数据集
    train_data = data[:train_samples]
    valid_data = data[train_samples:train_samples + valid_samples]
    test_data = data[-test_samples:]

    return train_data, valid_data, test_data

def write_to_files(data, output_train, output_valid, output_test):
    with open(output_train, 'w', encoding='utf-8') as train_file:
        train_file.writelines(data[0])
    with open(output_valid, 'w', encoding='utf-8') as valid_file:
        valid_file.writelines(data[1])
    with open(output_test, 'w', encoding='utf-8') as test_file:
        test_file.writelines(data[2])

# 示例用法
input_txt = 'output.txt'
output_train = 'train.txt'
output_valid = 'dev.txt'
output_test = 'test.txt'
train_data, valid_data, test_data = split_dataset(input_txt)
write_to_files((train_data, valid_data, test_data), output_train, output_valid, output_test)
