# binary-search.py


# 二分查找法
# O(log n)
# 输入有序列表list与查找目标item，返回目标索引数
def binarySearch(list, item):
    low = 0
    high = len(list) - 1

    if list[low] > item:
        return None
    if list[high] < item:
        return None
    
    while low <= high:
        mid = int((low + high) / 2)
        guess = list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        elif guess < item:
            low = mid + 1
    return None

# 二分查找法递归版
def binarySearchRec(list, item):
    if len(list) == 0:
        return None
    
    low = 0
    high = len(list) - 1
    mid = int((low + high) / 2)
    guess = list[mid]

    if guess == item:
        return mid
    if len(list) == 1:
        if list[0] == item:
            return 0
        else:
            return None
    elif guess > item:
        return binarySearchRec(list[low:mid], item)
    elif guess < item:
        reult = binarySearchRec(list[mid+1:high], item)
        if reult == None:
            return reult
        else:
            return mid + 1 + binarySearchRec(list[mid+1:high], item)





# 搜寻数组中最小数
# 输入数组arr，返回数组最小索引号
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if smallest > arr[i]:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


# 选择排序法
# O(n^2)
# 输入数组arr，返回排序后的数组
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest_index = findSmallest(arr)
        newArr.append(arr.pop(smallest_index))
    return newArr

# 冒泡排序法
# O(n^2)
# 输入数组arr，返回排序后的数组
def bubbleSort(arr):
    for x in range(len(arr) - 1, -1, -1):
        for y in range(0, x):
            if arr[y] > arr[y+1]:
                temp = arr[y]
                arr[y] = arr[y+1]
                arr[y+1] = temp
    return arr


# 快速排序
#
def quickSort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]  # 基准值
    less = [i for i in arr[1:] if i <= pivot]       # 小于基准值存入数组
    greater = [i for i in arr[1:] if i > pivot]     # 大于基准值存入数组
    #for i in range(1, len(arr)):
    #    if arr[i] <= pivot:
    #        less.append(arr[i])
    #    elif arr[i] > pivot:
    #        greater.append(arr[i])
    
    return quickSort(less) + [pivot] + quickSort(greater)


# 阶乘函数
# 输入阶乘数x，返回阶乘结果
def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)


# 计算数组总和
# 输入数字数组，返回数字总和
def arrSum(arr):
    if len(arr) == 1:   # 如果数组长度为1，返回数组第一个元素
        return arr[0]
    if len(arr) == 0:   # 如果数组为0，返回0
        return 0
    num = arr.pop()
    return num + arrSum(arr)


# 斐波那契数
# 输入数字n
def fibseq(n):
    if n == 0:
        return 0
    if n < 3:
        return 1

    front = 1
    behind = 1
    fibN = 0
    for i in range(3, n+1):
        fibN = front + behind
        front = behind
        behind = fibN
    return fibN





# 读取输入并以int写入数组
#import sys
#
#arr = []
#for x in sys.stdin.readline().strip().split(' '):
#    arr.append(int(x))






# 计时算法
#import time
#
#time_start=time.time()
#
#time_end=time.time()
#print('totally cost',time_end-time_start)