#dfrom __future__ import annotations

class BinaryTree:
    def __init__(self, root_key):
        self.root = root_key
        self.left = None
        self.right = None

    def insert_left(left, left_child: BinaryTree) -> None:
        if self.left is None:
            self.left = left_child
        else:
            left_child.left = self.left
            self.left = left_child


    def insert_right(right, right_child: BinaryTree) -> None:
        if self.right is None:
            self.right = right_child
        else:
            right_child.right = self.right
            self.right = right_child

def get_root_val(self):
    return self.root

def set_root_val(self, new_root_val):
    self.root = new_root_val

def get_left_child(self) -> BinaryTree:
    return self.left

def get_right_child(self) -> BinaryTree:
    return self.right

def print_tree(self )
if __name__ = "__main__":
    a_tree = BinaryTree("a")
    print(a_tree.get_root_val())
    print(a_tree.get_left_child())

    b_tree = BinaryTree("b")
    a_tree.insert_left(b_tree)
    print(a_tree.get_left_child())
    print(a_tree.get_left_child().get_root_val())

