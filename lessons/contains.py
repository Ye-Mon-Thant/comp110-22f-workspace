"""An example of a list utility alogirithm."""

def contains(needle: str, haystack: list[str]) -> bool:
    i: int = 0
    while i < len(haystack):
        if needle == haystack[i]:
            return True        
        i += 1
    return False

