from typing import Union

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