class Node:

    def __init__(self, data):
        self.key = data
        self.next = None
        self.prev = None

    def compare(self, value):
        """method to compare the value with the node"""
        if self.data == value:
            return True
        else:
            return False


class DoubleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_item(self, item):
        if isinstance(item, Node):
            if self.head is None:
                self.head = item
                item.prev = None
                item.next = None
                self.tail = item
            else:
                self.tail.next = item
                item.prev = self.tail
                self.tail = item
        return

    def remove_item(self, item_id):
        pass
        
