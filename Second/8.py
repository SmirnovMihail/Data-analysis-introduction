class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, value=None):
        self.stack = list()
        if value:
            self.root = Node(value)
        else:
            self.root = None

    def __iter__(self):
        self.stack = list()
        self.stack.append(self.root)
        return self

    def __next__(self):
        if self.root is None:
            raise StopIteration
        if len(self.stack) == 0:
            self.stack.append(self.root)
            raise StopIteration
        val = self.stack.pop(0)
        if val.left is not None:
            self.stack.append(val.left)
        if val.right is not None:
            self.stack.append(val.right)
        return val.value

    def append(self, value):
        if self.root is None:
            self.root = Node(value)
            self.stack.append(self.root)
            return
        self.push_value(self.root, value)

    def push_value(self, current_node, value):
        if value < current_node.value:
            if current_node.left:
                self.push_value(current_node.left, value)
            else:
                current_node.left = Node(value)
        else:
            if current_node.right:
                self.push_value(current_node.right, value)
            else:
                current_node.right = Node(value)


# if __name__ == '__main__':
#     tree = BinarySearchTree()
#     for v in [8, 3, 10, 1, 6, 4, 14, 13, 7]:
#         tree.append(v)

#     for v in [8, 12, 13]:
#         print(v in tree)

#     print(*tree)

# if __name__ == '__main__':
#     tree = BinarySearchTree()
#     for v in [5, 0, 6, 2, 1, 3]:
#         tree.append(v)

#     for v in [6, 12]:
#         print(v in tree)

#     print(*tree)