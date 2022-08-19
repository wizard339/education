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

    def search(self, k):
        if self.root is None or k == self.key:
            return self.root.data
        if k < self.key:
            return self.search(self.left, k)
        else:
            return self.search(self.right, k)
    
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

    def delete(self):
        pass

    def minimum(self):
        pass

if __name__=='__main__':
    a = Node('First node', 10)
    print(a)
    b = BinTreeSearch()
    b.insert(50, 'This is fifty')
    
