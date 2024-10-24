class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
    # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      print(self.data),
      if self.right:
         self.right.PrintTree()

if __name__== "__main__":
    tree = [2, 12, 4, 5]
    binaryTree= Node(10)
    binaryTree.insert(5)
    for i in tree:
        binaryTree.insert(i)
    binaryTree.PrintTree()
