#二叉搜索树

class BiTreeNode:
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None
        self.parent = None

#插入
#使用递归
class BST:
    def __init__(self,li=None):
        self.root = None
        if li:
            for val in li:
                self.insert_no_rec(val)

    def insert(self,root,val):
        if not node:
            node = BiTreeNode(val)
        if val < node.data:
            node.lchild = self.insert(node.lchild,val)
            node.lchild.parent = node
        elif val > node.data:
            node.rchild = self.insert(node.rchild,val)
            node.rchild.parent = node
        return node

#不使用递归
    def insert_no_rec(self,val):
        p = self.root
        if not p:               #空树
            self.root = BiTreeNode(val)
            return
        while True:
            if val < p.data:
                if p.lchild:
                    p = p.lchild
                else:         #左孩子不存在
                    p.lchild = BiTreeNodea(val)
                    p.lchild.parent = p
                    return
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = BiTreeNode(val)
                    p.rchild.parent = p
                    return
            else:
                return


#查询
#递归
    def query(self,node,val):
        if not node:
            return None
        if node.data < val:
            return self.query(node.rchild,val)
        elif node.data > val:
            return self.query(node.lchild,val)
        else:
            return node

#非递归
    def query_no_sec(self,val):
        p = self.root
        while p:
            if p.data < val:
                p = p.rchild
            elif p.data > val:
                p = p.lchild
            else:
                return p


tree = BST[4,6,7,9,2,1,3,5,8]

