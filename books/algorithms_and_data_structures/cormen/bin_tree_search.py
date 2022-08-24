import dataclasses
from typing import Any, Optional, Union


@dataclasses.dataclass
class Node:
    key: Any
    data: Any
    left: Optional["Node"] = None
    right: Optional["Node"] = None
    parent: Optional["Node"] = None


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
            else:
                current = current.right
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

    def transplant(self, deleting_node: Optional["Node"], replacing_node: Optional["Node"]) -> None:
        """the method is needed to replace one subtree with another subtree"""
        if deleting_node.parent is None:
            self.root = replacing_node
        elif deleting_node == deleting_node.parent.left:
            deleting_node.parent.left = replacing_node
        else:
            deleting_node.parent.right = replacing_node
        if replacing_node:
            replacing_node.parent = deleting_node.parent
    
    def delete(self, deleting_node: Optional["Node"]) -> None:
        """the method is required to delete a node"""
        # Case 1: no child or Case 2a: only one right child
        if deleting_node.left is None:
            self.transplant(deleting_node, deleting_node.right)
        # Case 2b: only one left left child
        elif deleting_node.right is None:
            self.transplant(deleting_node, deleting_node.left)
        # Case 3: two children
        else:
            successor_node = self.minimum(deleting_node.right)
            if successor_node.parent != deleting_node:
                self.transplant(successor_node, successor_node.right)
                successor_node.right = deleting_node.right
                successor_node.right.parent = successor_node
            self.transplant(deleting_node, successor_node)
            successor_node.left = deleting_node.left
            successor_node.parent = successor_node

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

    b.delete(b.search(30))
    print('After deleting 30:')
    b.inorder_walk(b.root)
    b.delete(b.search(77))
    print('After deleting 77:')
    b.inorder_walk(b.root)
    
    print(f'Successor of the node "50": {b.maximum(b.search(50))}')
    print(f'Predecessor of the node "50": {b.predecessor(b.search(50))}')
