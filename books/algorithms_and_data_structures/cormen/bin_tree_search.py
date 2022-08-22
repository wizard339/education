import dataclasses
from typing import Any, Optional, Union


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
        """the method gets the key and returns a pointer to the node with this key """
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

    def inorder_walk(self, root: Optional["Node"]) -> None:
        current = root
        if current:
            self.inorder_walk(current.left)
            print(current.key)
            self.inorder_walk(current.right)

    def delete(self):
        pass

    def minimum(self, node: Optional["Node"]) -> Optional["Node"]:
        """the method returns a pointer to the minimum element of the subtree"""
        while node.left:
            node = node.left
        return node

    def maximum(self, node: Optional["Node"]) -> Optional["Node"]:
        """the method returns a pointer to the maximum element of the subtree"""
        while node.right:
            node = node.right
        return node

    def successor(self, node: Optional["Node"]) -> Optional["Node"]:
        """
        the method gets a pointer to the node and returns a pointer to the
        successor-node
        """
        if node.right:
            return self.minimum(node.right)
        res = node.parent
        while res and node == res.right:
            node = res
            res = res.parent
        return res

    def predecessor(self, node: Optional["Node"]) -> Optional["Node"]:
        """
        the method gets a pointer to the node and returns a pointer to the
        successor-node
        """
        if node.left:
            return self.maximum(node.left)
        res = node.parent
        while res and node == res.left:
            node = res
            res = res.parent
        return res


if __name__=='__main__':
    b = BinTreeSearch()
    b.insert(50, 'This is fifty')
    b.insert(10, 'This is ten')
    b.insert(70, 'This is seventy')
    b.insert(15, 'This is fifteen')
    b.insert(30, 'This is thirty')
    b.insert(40, 'This is fourty')
    b.insert(60, 'This is sixty')
    b.insert(77, 'This is seventy seven')
    b.inorder_walk(b.root)

    print(f'Successor of the node "50": {b.successor(b.search(50))}')
    print(f'Predecessor of the node "50": {b.predecessor(b.search(50))}')
