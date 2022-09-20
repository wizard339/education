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
    size: int = 1


class OrderStatTree:
    def __init__(self) -> None:
        self.null: Optional["Node"] = Node(key=0, data=None, color="black", size=0)
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
        # size support
        y.size = x.size
        x.size = x.left.size + x.right.size + 1

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
        # size support
        x.size = y.size
        y.size = y.left.size + y.right.size + 1

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
            # size support
            parent.size += 1
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

    def transplant(self, deleting_node: Optional["Node"],
                   replacing_node: Optional["Node"]) -> None:
        """the method is needed to replace one subtree with another subtree"""
        if deleting_node.parent == self.null:
            self.root = replacing_node
        elif deleting_node == deleting_node.parent.left:
            deleting_node.parent.left = replacing_node
        else:
            deleting_node.parent.right = replacing_node
        replacing_node.parent = deleting_node.parent
        # size support
        replacing_node.size = deleting_node.size - 1

    def minimum(self, x: Optional["Node"]) -> Optional["Node"]:
        """the method returns a pointer to the minimum element of the subtree"""
        while x.left != self.null:
            x = x.left
        return x

    def delete(self, deleting_node: Optional["Node"]) -> None:
        y = deleting_node
        y_origin_color = y.color
        if deleting_node.left == self.null:
            x = deleting_node.right
            self.transplant(deleting_node, deleting_node.right)
        elif deleting_node.right == self.null:
            x = deleting_node.left
            self.transplant(deleting_node, deleting_node.left)
        else:
            y = self.minimum(deleting_node.right)
            y_origin_color = y.color
            x = y.right
            if y.parent == deleting_node:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = deleting_node.right
                y.right.parent = y
            self.transplant(deleting_node, y)
            y.left = deleting_node.left
            y.left.parent = y
            y.color = deleting_node.color

        if y_origin_color == "black":
            self.delete_fixup(x)

        # size support
        while y != self.root:
            y = y.parent
            y.size -= 1

    def delete_fixup(self, x: Optional["Node"]) -> None:
        """the method is necessary to preserve the red-black properties after deleting"""
        while x != self.root and x.color == "black":
            if x == x.parent.left:
                w = x.parent.right
                # case 1
                if w.color == "red":
                    w.color = "black"
                    x.parent.color = "red"
                    self.left_rotate(x.parent)
                    w = x.parent.right
                # case 2
                if w.left.color == "black" and w.right.color == "black":
                    w.color = "red"
                    x = x.parent
                # case 3
                else:
                    if w.right.color == "black":
                        w.left.color = "black"
                        w.color = "red"
                        self.right_rotate(w)
                        w = x.parent.right
                    # case 4
                    w.color = x.parent.color
                    x.parent.color = "black"
                    w.right.color = "black"
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                # case 1
                if w.color == "red":
                    w.color = "black"
                    x.parent.color = "red"
                    self.right_rotate(x.parent)
                    w = x.parent.left
                # case 2
                if w.right.color == "black" and w.left.color == "black":
                    w.color = "red"
                    x = x.parent
                # case 3
                else:
                    if w.left.color == "black":
                        w.right.color = "black"
                        w.color = "red"
                        self.left_rotate(w)
                        w = x.parent.left
                    # case 4
                    w.color = x.parent.color
                    x.parent.color = "black"
                    w.left.color = "black"
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = "black"

    def inorder_walk(self, root: Optional["Node"]) -> None:
        current = root
        if current and current != self.null:
            self.inorder_walk(current.left)
            print(current.key)
            self.inorder_walk(current.right)

    def search(self, key: Any) -> Optional["Node"]:
        current = self.root
        while current and key != current.key:
            if key < current.key:
                current = current.left
            else:
                current = current.right
        return current

    def select(self, x: Optional["Node"], i: int) -> Optional["Node"]:
        """
        the method searches for an element with the i-rank and returns a pointer to the node
        with the i-th element in ascending order in the subtree, where x is the root
        """
        if x.left is not None:
            r = x.left.size + 1
            if i == r:
                return x
            elif i < r:
                return self.select(x.left, i)
            else:
                return self.select(x.right, i - r)
        else:
            return x

    def rank(self, x: Optional["Node"]) -> int:
        r = x.left.size + 1
        y = x
        while y != self.root:
            if y == y.parent.right:
                r += y.parent.left.size + 1
            y = y.parent
        return r


if __name__ == '__main__':
    b = OrderStatTree()
    b.insert(50, 'This is fifty')
    b.insert(10, 'This is ten')
    b.insert(70, 'This is seventy')
    b.insert(15, 'This is fifteen')
    b.insert(30, 'This is thirty')
    b.insert(40, 'This is fourty')
    b.insert(60, 'This is sixty')
    b.insert(77, 'This is seventy seven')

    b.inorder_walk(b.root)
    print('Insertion completed')

    node_to_delete = b.search(10)
    b.delete(node_to_delete)
    print(f'Deleting the next element: {node_to_delete.key}')

    b.inorder_walk(b.root)

    print(b.select(b.root, 3).key)

    # building a tree
    print(6*'\t' + f'Root of the tree: key {b.root.key}, size {b.root.size}')
    
    print(6*'\t' + '/' + 8*'\t' + '\\')
    
    print(5*'\t' + f'key {b.root.left.key}' + 8*'\t' +
          f'key {b.root.right.key}')
    print(5*'\t' + f'size {b.root.left.size}' + 8*'\t' +
          f'size {b.root.right.size}')
    
    print(3*'\t' + '/' + 5*'\t' + '\\' + 4*'\t' + '/' + 5*'\t' + '\\')
    
    print(2*'\t' + f'key {b.root.left.left.key}' + 4*'\t' +
          f'key {b.root.left.right.key}' + 4*'\t' +
          f'key {b.root.right.left.key}' + 4*'\t' + 
          f'key {b.root.right.right.key}')
    print(2*'\t' + f'size {b.root.left.left.size}' + 4*'\t' +
          f'size {b.root.left.right.size}' + 4*'\t' +
          f'size {b.root.right.left.size}' + 4*'\t' + 
          f'size {b.root.right.right.size}')

    print(1*'\t' + '/' + 3*'\t' + '\\' + 2*'\t' + '/' + 3*'\t' + '\\' +
          2*'\t' + '/' + 3*'\t' + '\\' + 2*'\t' + '/' + 3*'\t' + '\\')

    print(f'key {b.root.left.left.left.key}' + 2*'\t' +
          f'key {b.root.left.left.right.key}' + 1*'\t' +
          f'key {b.root.left.right.left.key}' + 2*'\t' +
          f'key {b.root.left.right.right.key}' + 2*'\t' +
          f'key {b.root.right.left.left.key}' + 2*'\t' +
          f'key {b.root.right.left.right.key}' + 1*'\t' +
          f'key {b.root.right.right.left.key}' + 2*'\t' +
          f'key {b.root.right.right.right.key}')
    print(f'size {b.root.left.left.left.size}' + 2*'\t' +
          f'size {b.root.left.left.right.size}' + 1*'\t' +
          f'size {b.root.left.right.left.size}' + 2*'\t' +
          f'size {b.root.left.right.right.size}' + 2*'\t' +
          f'size {b.root.right.left.left.size}' + 2*'\t' +
          f'size {b.root.right.left.right.size}' + 1*'\t' +
          f'size {b.root.right.right.left.size}' + 2*'\t' +
          f'size {b.root.right.right.right.size}')
