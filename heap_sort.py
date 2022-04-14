#堆排序-树与二叉树
#二叉树：度不超过2的树，每个节点最多两个孩子节点
#满二叉树：一个二叉树每个层的节点都是最大值，就是满二叉树
#完全二叉树：从满二叉树最后拿走几个节点
#堆是一种特殊的完全二叉树结构
#大根堆：一棵完全二叉树，满足任意节点都比其孩子节点大
#小根堆：一棵完全二叉树，满足任意节点都比其孩子节点小

#堆排序过程
# 1.建立堆（农村包围城市，右下角最小的开始）
# 2.得到堆顶元素，为最大元素
# 3.去掉堆顶，将堆最后一个元素放到堆顶，此时可通过一次调整重新使堆有序
# 4.堆顶元素为第二大元素
# 5.重复step3，直到堆边空

'''向下调整代码'''
def sift(li,low,high):   #堆的最后一个元素的下标是high，第一个元素的下标是low
    """
    :param li: 列表
    :param low: 堆的根节点位置（堆顶）
    :param high: 堆的最后一个元素的位置
    :return:
    """
    i = low #i最开始指向根节点
    j = 2 * i + 1  #j是左孩子，父找子
    tmp = li[low] #把堆顶的存起来
    while j <= high: #只要j位置有数，就一直循环
        if j + 1 <= high and li[j+1] > li[j]: #如果右孩子有并且比较大
            j = j + 1  #j指向右孩子
        if li[j] > tmp:
            li[i] = li[j]
            i = j           #往下看一层
            j= 2 * i + 1
        else:       #tmp更大，把tmp放到i的位置上
            li[i] = tmp
            break
    else:
        li[i] = tmp

def heap_sort(li):
    n = len(li)
    for i in range((n-2)//2,-1,-1):  #子找父
        # i 表示建堆的时候调整的部分的根的下标
        sift(li,i,n-1)   #high就是最后一个元素的元素下标
    #建堆完成
    for i in range(n-1,-1,-1):
        # i 指向当前堆的最后一个元素
        li[0],li[i] = li[i],li[0]
        sift(li,0,i-1)  #i-1是新的high

li = [i for i in range(100)]
import random
random.shuffle(li)
print(li)

heap_sort(li)