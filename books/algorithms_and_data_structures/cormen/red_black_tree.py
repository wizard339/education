import dataclasses
from typing import Any, Optional, Union


@dataclasses.dataclass
class Node:
    key: Any
    data: Any
    color: Union["black", "red"] = None
    left: Optional["Node"] = None
    right: Optional["Node"] = None
    parent: Optional["Node"] = None


class RedBlackTree:
    def __init__(self) -> None:
        self.null: Optional["Node"] = Node(key=0, data=None, color="black")
        self.root: Optional["Node"] = self.null

    def left_rotate(self, x: Optional["Node"]) -> None:
        """the method is needed to save property of the black-red tree"""
        y = x.right
        # the left subtree of y becomes the right subtree of x
        x.right = y.left
        if y.left != self.null:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.null:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        # placing x as the left child node
        x.parent = y
            
    def right_rotate(self, y: Optional["Node"]) -> None:
        """the method is needed to save property of the black-red tree"""
        x = y.left
        y.left = x.right
        if x.right != self.null:
            x.right.parent = y
        x.parent = y.parent
        if y.parent == self.null:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x
    
    def insert(self, key: Any, data: Any) -> None:
        new_node = Node(key=key, data=data)
        parent: Optional["Node"] = self.null
        current: Optional["Node"] = self.root
        while current != self.null:
            parent = current
            if new_node.key < current.key:
                current = current.left
            else:
                current = current.right
        new_node.parent = parent
        # if tree is empty
        if parent == self.null:
            self.root = new_node
            self.root.parent = None
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node
        new_node.left = self.null
        new_node.right = self.null
        new_node.color = "red"
        self.insert_fixup(new_node)

    def insert_fixup(self, new_node: Optional["Node"]) -> None:
        """the method is necessary to preserve the red-black properties after insertion"""
        while new_node != self.root and new_node.parent.color == "red":
            if new_node.parent == new_node.parent.parent.left:
                y = new_node.parent.parent.right
                # case 1 - "uncle" of new_node is red
                if y.color == "red":
                    new_node.parent.color = "black"
                    y.color = "black"
                    new_node.parent.parent.color = "red"
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.right:
                        # case 2 - "uncle" of new_node is black and new_node is right child
                        new_node = new_node.parent
                        self.left_rotate(new_node)
                    # case 3 - "uncle" of new_node is black and new_node is left child
                    new_node.parent.color = "black"
                    new_node.parent.parent.color = "red"
                    self.right_rotate(new_node.parent.parent)
            else:
                y = new_node.parent.parent.left
                # case 1
                if y.color == "red":
                    new_node.parent.color = "black"
                    y.color = "black"
                    new_node.parent.parent.color = "red"
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.left:
                        # case 2
                        new_node = new_node.parent
                        self.right_rotate(new_node)
                    # case 3
                    new_node.parent.color = "black"
                    new_node.parent.parent.color = "red"
                    self.left_rotate(new_node.parent.parent)
        self.root.color = "black"

    def inorder_walk(self, root: Optional["Node"]) -> None:
        current = root
        if current and current != self.null:
            self.inorder_walk(current.left)
            print(current.key)
            self.inorder_walk(current.right)


if __name__=='__main__':
    b = RedBlackTree()
    b.insert(50, 'This is fifty')
    b.insert(10, 'This is ten')
    b.insert(70, 'This is seventy')
    b.insert(15, 'This is fifteen')
    b.insert(30, 'This is thirty')
    b.insert(40, 'This is fourty')
    b.insert(60, 'This is sixty')
    b.insert(77, 'This is seventy seven')

    b.inorder_walk(b.root)
    
