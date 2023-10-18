import math
import numpy as np

# 打开txt文件进行读取
with open('./都市逍遥仙帝.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# 计算文本内容的20%所对应的字符数
total_len = len(content)
print(total_len)
start_index = 0


for rat in np.arange(0, 0.2, 0.02):
    start_index = int(rat * total_len)
    end_index = math.ceil(total_len * (rat + 0.02))

    # 截取文本的前20%内容
    first_20pct = content[start_index:end_index]

    with open('./part_dsxytd/output_{:.2f}.txt'.format(rat), 'w', encoding='utf-8') as f:
        f.write(first_20pct)