from typing import TypeVar
T = TypeVar('T')
def get_first_element(items: list[T]) -> T:
    return items[0]



nums = [1, 2, 3]
srings = ["a", "b", "c"]

print(get_first_element(nums))  # Output: 1
print(get_first_element(srings))  # Output: "a"

#1. will pass a list where all the itmem will have the same type
#2. <T> is fill in he blank. <T> will be whatever type we define.
#3 whatever type of <T> will be returned.