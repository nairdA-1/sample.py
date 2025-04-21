from binary_tree import BinaryTree
from stack import Stack

def parse_expression(expression: str) -> BinaryTree:
    s = Stack()
    bt = BinaryTree(None)

    s.push(bt)

    tokens = expression.split()
    print(tokens)

    for token in tokens:
        if token == "(":
            current_bt.insert_left(BinaryTree(None))
            s.push(current_bt)
            current_bt = current_bt.get_left_child()

        elif token in 