#汉诺塔问题
#1.把n-1个圆盘从A经过C移动到B
#2.把第n个圆盘从A移动到C
#3.把n-1个圆盘从A移动到C

def hanoi(n,a,b,c):
    if n>0:
        hanoi(n-1,a,c,b)
        print("moving from %s to %s"%(a,c))

hanoi(3,'A','B','C')