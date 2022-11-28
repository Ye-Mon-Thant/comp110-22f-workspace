from typing import Union
from typing import Optional

def add(lhs: float = 0.0, rhs: Union[str, float] = 0.0) -> float:
    result: float = lhs
    if isinstance(rhs, str):
        result += float(rhs)
    else:
        result += rhs
    return result

add()
add(1.0)
add(1.0, 2.0)
#add("2.0", 1.0)
add(2.0, "1.0")
print(add(110.0))
print(add(110.0, "100.0"))

list1 = [2, 3, 4, 5]
list1[2] = 0
print(list1)


class apple():
    eggs: list[str] 
    def __init__(self, opp : Optional[list]) -> None:
        if isinstance(opp, list):
            print("yes")
            self.eggs = opp
        else:
            self.eggs = []

            
            print("no")

dog = apple([1,3,5])

