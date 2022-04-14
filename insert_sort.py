#插入排序
#类似斗地主摸牌
#复杂度O（n方）

def insert_sort(li):
    for i in range(1,len(li)):   #i表示摸到的牌的下标
        tmp = li[i]
        j = i-1  #j指的是手里的牌的下标
        while j>=0 and li[j] > tmp:  #找插入的位置
            li[j+1]=li[j]
            j -= 1
        li[j+1] = tmp

li = [3,2,4,1,5,7,9,6,8]
insert_sort(li)
print(li)