# gen.py
# 生成一堆数字，用于测试排序与查找算法

import random

for x in range(1, 50000):
    print(random.randint(1, 100000000), end=' ')

# 生成有序数组
#for x in range(1, 50000):
#    print(x, end=' ')