from __future__ import annotations

from typing import Union, Optional

class Node:
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return f'{self.data} -> {self.next}'



def someom(dict0):
    dict0['apple'] = 10


def sum(node: Optional[Node]) -> int:
    result: int = 0
    if node == None:
        return 0
    else:
        return node.data + sum(node.next)

def count(node: Optional[Node], current_count: int = 0) -> int:
    if node is None:
        return current_count
    else:
        return count(node.next, current_count + 1)
        

head: Node = Node(3, None)
head = Node(2, head)
head = Node(1, head)
block = head
block.data = 9
block = Node(8, block)
print(block, head)
print(sum(head))
print(count(head))
print(head)

list_1 = [1,2,3]
list_2 = list_1
list_2.append(9)
print(list_1, list_2)

dict1 = {'apple' : 110}
dict2 = dict1
dict2['bana'] = 120
someom(dict2)
dict2.pop('bana')
print(dict2, dict1)

def mom(dict0):
    dict0['apple'] = 10

