import heapq
import dataclasses
from collections import Counter
from typing import Optional


@dataclasses.dataclass
class Node:
    freq: int = None
    char: str = None
    left: Optional["Node"] = None
    right: Optional["Node"] = None

    # override the magic method to create conditions for using the heapq structure from the Python standard library
    def __lt__(self, other):
        return self.freq < other.freq


def huffman_encode(data: str) -> list:
    h = []
    
    # calculating character frequencies and putting them in a list
    for char, freq in sorted(Counter(data).items(), key=lambda x: x[1]):
        h.append(Node(freq, char))
        
    # creating a binary tree
    heapq.heapify(h)
    n = len(h)
    
    for i in range(1, n):
        # creating a new node
        z = Node()
        z.left = heapq.heappop(h)
        z.right = heapq.heappop(h)
        z.freq = z.left.freq + z.right.freq
        heapq.heappush(h, z)

    # return the root of the tree
    return heapq.heappop(h)


if __name__ == '__main__':
    a = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbccccccccccccddddddddddddddddeeeeeeeeefffff'
    print(huffman_encode(a))
