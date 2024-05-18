import csv

def csv_to_txt(input_csv, output_txt):
    with open(input_csv, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # 跳过第一行（标题行）
        with open(output_txt, 'w', encoding='utf-8') as txt_file:
            for row in reader:
                # 替换回车换行符和制表符为空格
                cleaned_row = [' '.join(cell.splitlines()).replace('\t', ' ') for cell in row]
                # 在每行的两列之间使用制表符分隔
                txt_file.write('\t\t'.join(cleaned_row) + '\n')

# 示例用法
input_csv = 'val.csv'
output_txt = 'output.txt'
csv_to_txt(input_csv, output_txt)

