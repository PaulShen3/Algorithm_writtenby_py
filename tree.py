


class Node:
    def __init__(self,name,type='dir'):
        self.name = name
        self.type = type  #dir or file
        self.children = []
        self.parent = None   #不能往回找


class FileSystemTree:
    def __init__(self):
        self.root = Node("/")
        self.now = self.root

    def mkdir(self,name):
        #name必须是以/结尾
        if name[-1] != "/":
            name += "/"
        node = Node(name)
        self.now.children.append(node)
        node.parent = self.now

    def ls(self):
        return self.now.children

    def cd(self,name):
        if name[-1] != "/":
            name += "/"
        if name == "../":
            self.now = self.now.parent
            return
        for child in self.now.children:
            if child.name == name:
                self.now = child
                return
        raise ValueError("invalid dir")


tree = FileSystemTree()
tree.mkdir("var/")
tree.mkdir("bin/")
tree.mkdir("usr/")

tree.cd("bin/")

tree.cd("../")
tree.mkdir("python")

print(tree.ls())


# n = Node("hello")
# n2 = Node("world")
# n.children.append(n2)
# n2.parent = n