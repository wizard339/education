import dataclasses
from typing import Any, Optional


@dataclasses.dataclass
class Node:
    key: Any
    data: Any
    left: Optional["Node"] = None
    right: Optional["Node"] = None
    parent: Optional["Node"] = None


class DuplicateKeyError(Exception):
    def __init__(self, key: str) -> None:
        Exception.__init__(self, f"{key} already exists.")


class BinTreeSearch:
    def __init__(self) -> None:
        self.root: Optional["Node"] = None

    def search(self, key: Any) -> Optional["Node"]:
        current = self.root
        while current and key != current.key:
            if key < current.key:
                current = current.left
            else:
                current = current.right
        return current
    
    def insert(self, key: Any, data: Any) -> None:
        new_node = Node(key=key, data=data)
        parent: Optional["Node"] = None
        current: Optional["Node"] = self.root
        while current:
            parent = current
            if new_node.key < current.key:
                current = current.left
            elif new_node.key > current.key:
                current = current.right
            else:
                raise DuplicateKeyError(key=new_node.key)
        new_node.parent = parent
        # if tree is empty
        if parent is None:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

    def inorder_walk(self, root):
        current = root
        if current:
            self.inorder_walk(current.left)
            print(current.key)
            self.inorder_walk(current.right)

    def delete(self):
        pass

    def minimum(self):
        pass

if __name__=='__main__':
    b = BinTreeSearch()
    b.insert(50, 'This is fifty')

    b.insert(10, 'This is ten')

    b.insert(70, 'This is seventy')

    
    print(b.search(10))
    b.inorder_walk(b.root)
