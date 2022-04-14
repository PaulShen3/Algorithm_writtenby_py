#快速排序  时间复杂度O（nlogn）
#取第一个元素p，使元素p归为，列表被分为两部分，左边小于p，右边大于p，递归完成排序
import random

def partition(li,left,right):
    tmp = li[left]
    while left < right:
        """下面这个left<right的是为了防止右边的全都比left大导致无法退出循环"""
        while left < right and li[right] >= tmp:  #从右边找比tmp小的数
            right -= 1      #往左走一步
        li[left] = li[right]   #把右边的值写到左边空位上
        print(li,'right')
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]  #把左边的值写到右边空位上
        print(li,'left')
    li[left] = tmp
    return left   #返回left和right都可以

def quick_sort(li,left,right):
    if left < right:
        mid = partition(li,left,right)
        quick_sort(li,left,mid-1)
        quick_sort(li,mid+1,right)

li = [5,7,4,6,3,1,2,9,8]
quick_sort(li,0,len(li)-1)
print(li)

li = list(range(10000))
random.shuffle(li)