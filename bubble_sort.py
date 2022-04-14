#冒泡排序

def bubble_set(li):
    for i in range(len(li)-1):
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
                exchange = True
        print(li)
        if not exchange:
            return None

bubble_set([1,3,4,3,6,2,4,7,5,7,9])