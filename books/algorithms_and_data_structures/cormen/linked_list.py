class Node:
    """
    The class for node of the linked list.
    
    Description of the attributes of the class:
    `key` is the data of the node;
    `next` is the pointer on the next node in the linked list;
    `prev` is the pointer on the previous node in the linked list
    """
    def __init__(self, data):
        self.key = data
        self.next = None
        self.prev = None

    def compare(self, value):
        """the method to compare the value with the node"""
        if self.data == value:
            return True
        else:
            return False


class DoubleLinkedList:
    """
    The class for a doubly linked list.
    The attribute `head` is the pointer on the first node.
    """
    def __init__(self):
        self.head = None

    def search(self, k):
        """the method of searching for a node by node's data"""
        x = self.head
        while x is not None and x.key != k:
            x = x.next
        try:
            if x.key == k:
                return x
        except:
            raise KeyError('This item is not in the list!')

    def insert(self, x):
        """the method of inserting node in the head of the list"""
        if not isinstance(x, Node):
            x = Node(x)
        x.next = self.head
        if self.head is not None:
            self.head.prev = x
        self.head = x
        x.prev = None

    def delete_by_item(self, x):
        """the method of deleting node by the node's pointer"""
        if x.prev is not None:
            x.prev.next = x.next
        else:
            self.head = x.next
        if x.next is not None:
            x.next.prev = x.prev

    def delete_by_key(self, k):
        """the method of deleting node by the node's data"""
        x = self.search(k)
        self.delete_by_item(x)


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    linked_list = DoubleLinkedList()
    linked_list.insert(node1)
    linked_list.insert(node2)
    linked_list.insert(node3)
    print(linked_list.search(2))
    print(node2)
    linked_list.insert(10)
    print(linked_list.search(10))
    linked_list.delete_by_item(node2)
    linked_list.delete_by_key(10)
    print(linked_list.search(10))
