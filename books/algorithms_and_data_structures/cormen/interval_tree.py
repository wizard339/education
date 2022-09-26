import dataclasses
from typing import Any, Optional, Union


@dataclasses.dataclass
class Node:
    # the interval with two ends: low and high
    interval: Union["list", "tuple"] = (-float('inf'), -float('inf'))
    # lower end of the interval
    low: float = interval[0]
    # higher end of the interval
    high: float = interval[1]
    color: Union["black", "red"] = None
    left: Optional["Node"] = None
    right: Optional["Node"] = None
    parent: Optional["Node"] = None
    max: float = high


class IntervalTree:
    def __init__(self) -> None:
        self.null: Optional["Node"] = Node(color="black")
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
        # attribute 'max' support
        x.max = max(x.high, x.left.max, x.right.max)
        y.max = max(y.high, y.left.max, y.right.max)
            
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
        # attribute 'max' support
        x.max = max(x.high, x.left.max, x.right.max)
        y.max = max(y.high, y.left.max, y.right.max)
    
    def insert(self, interval: Union["list", "tuple"]) -> None:
        new_node = Node(interval=interval, low=interval[0], high=interval[1], max=interval[1])
        parent: Optional["Node"] = self.null
        current: Optional["Node"] = self.root
        while current != self.null:
            parent = current
            current.max = max(current.max, new_node.max)
            if new_node.low < current.low:
                current = current.left
            else:
                current = current.right
        new_node.parent = parent
        # if tree is empty
        if parent == self.null:
            self.root = new_node
            self.root.parent = None
        elif new_node.low < parent.low:
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

    def transplant(self, deleting_node: Optional["Node"], replacing_node: Optional["Node"]) -> None:
        """the method is needed to replace one subtree with another subtree"""
        if deleting_node.parent == self.null:
            self.root = replacing_node
        elif deleting_node == deleting_node.parent.left:
            deleting_node.parent.left = replacing_node
        else:
            deleting_node.parent.right = replacing_node
        replacing_node.parent = deleting_node.parent

    def minimum(self, x: Optional["Node"]) -> Optional["Node"]:
        """the method returns a pointer to the minimum element of the subtree"""
        while x.left != self.null:
            x = x.left
        return x

    def delete(self, deleting_node: Optional["Node"]) -> None:
        y = deleting_node
        y_origin_color = y.color
        if deleting_node.left == self.null:
            # size support
            z = y
            while z != self.root:
                z.max = max(z.max, z.left.max, z.right.max)
                z = z.parent
                
            x = deleting_node.right
            self.transplant(deleting_node, deleting_node.right)
        elif deleting_node.right == self.null:
            # size support
            z = y
            while z != self.root:
                z.max = max(z.max, z.left.max, z.right.max)
                z = z.parent
                
            x = deleting_node.left
            self.transplant(deleting_node, deleting_node.left)
        else:
            # size support
            z = y
            while z != self.root:
                z.max = max(z.max, z.left.max, z.right.max)
                z = z.parent
                
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
            print(current.interval)
            self.inorder_walk(current.right)

    def search(self, low: Any) -> Optional["Node"]:
        current = self.root
        while current and low != current.low:
            if low < current.low:
                current = current.left
            else:
                current = current.right
        return current


if __name__=='__main__':
    b = IntervalTree()
    b.insert([50, 75])
    b.insert([10, 34])
    b.insert([70, 76])
    b.insert([15, 44])
    b.insert([30, 91])
    b.insert([40, 76])
    b.insert([60,104])
    b.insert([77, 90])

    b.inorder_walk(b.root)
    print('Insertion completed')


    # node_to_delete = b.search(30)
    # b.delete(node_to_delete)
    # print(f'Deleting the next element: {node_to_delete.interval}')
    
    # b.inorder_walk(b.root)


    def build_tree():
        # building a tree
        print(6*'\t' + f'Root: interval {b.root.interval}, max {b.root.max}')
        
        print(6*'\t' + '/' + 8*'\t' + '\\')
        
        print(5*'\t' + f'{b.root.left.interval}' + 7*'\t' +
              f'{b.root.right.interval}')
        print(5*'\t' + f'max {b.root.left.max}' + 8*'\t' +
              f'max {b.root.right.max}')
        
        print(3*'\t' + '/' + 5*'\t' + '\\' + 5*'\t' + '/' + 5*'\t' + '\\')
        
        print(2*'\t' + f'{b.root.left.left.interval}' + 4*'\t' +
              f'{b.root.left.right.interval}' + 2*'\t' +
              f'{b.root.right.left.interval}' + 3*'\t' + 
              f'{b.root.right.right.interval}')
        print(2*'\t' + f'max {b.root.left.left.max}' + 5*'\t' +
              f'max {b.root.left.right.max}' + 3*'\t' +
              f'max {b.root.right.left.max}' + 4*'\t' + 
              f'max {b.root.right.right.max}')
    
        print(1*'\t' + '/' + 3*'\t' + '\\' + 3*'\t' + '/' + 3*'\t' + '\\' +
              2*'\t' + '/' + 2*'\t' + '\\' + 2*'\t' + '/' + 3*'\t' + '\\')

        print(9*'\t' + f'{b.root.left.right.right.interval}')
        print(9*'\t' + f'max {b.root.left.right.right.max}')
        
    build_tree()
