#选择排序
def select_sort(li):
    for i in range(len(li)-1):
        min_loc = i
        for j in range(i,len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
            li[i],li[min_loc] = li[min_loc],li[i]

li = [1,2,4,5,1,6,2,7,9,5]
print(select_sort(li))