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


class BlackRedTree:
    def __init__(self) -> None:
        self.root: Optional["Node"] = None

    def left_rotate(self, node: Optional["Node"]) -> None:
        pass

    def right_rotate(self, node: Optional["Node"]) -> None:
        pass
    
    def insert(self, key: Any, data: Any) -> None:
        pass


if __name__=='__main__':
    b = BlackRedTree()
    
