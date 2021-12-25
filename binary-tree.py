
class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # def insert(self, data):
    #     if self.data:
    #         if data < self.data:
    #             if self.left is None:
    #                 self.left = Node(data)
    #             else:
    #                 self.left.insert(data)
    #         else:
    #             if self.right is None:
    #                 self.right = Node(data)
    #             else:
    #                 self.right.insert(data)
    #     else:
    #         self.data = data
    

    def insert(self, root, data):
        if root is None:
            root = self.Node(data)
            return root
        else:
            if data < root.data:
                if root.left is None:
                    root.left = Node(data)
                else:
                    self.insert(root.left, data)
            else:
                if root.right is None:
                    root.right = Node(data)
                else:
                    self.insert(root.right, data)
        return root

    def printInorder(self, root):
        if root.left:
            self.printInorder(root.left)
        print(root.data)
        if root.right:
            self.printInorder(root.right)

    def printPreorder(self, root):
        print(root.data)
        if root.left:
            self.printPreorder(root.left)
        if root.right:
            self.printPreorder(root.right)  

    def printPostorder(self, root):
        if root.left:
            self.printPostorder(root.left)
        if root.right:
            self.printPostorder(root.right)  
        print(root.data)  

    # def levelOrder(self, root):
    #     que = []
    #     que.append(root.data)
    #     curr = que.pop(0)
    #     if curr is None:

    def sumNodes(self, root):
        if root == None:
            return 0
        else:
            return self.sumNodes(root.left) + self.data + self.sumNodes(root.right)



root  = Node(27)
root.insert(root, 14)
root.insert(root, 35)
root.insert(root, 10)
root.insert(root, 19) 
root.insert(root, 31)
root.insert(root, 42)
print('PreOrder')
root.printPreorder(root)
print('InOrder')
root.printInorder(root)
print('PostOrder')
root.printPreorder(root)
print(f'Sum of Nodes : {root.sumNodes(root)}')