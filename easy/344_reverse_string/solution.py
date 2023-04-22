from typing import List

def reverse_string(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    # easy solution
    # s.reverse()

    end_index = len(s) - 1
    for count in range(len(s) // 2):
        s[end_index], s[end_index - (len(s) // 2)]
        end_index -= 1


if "__main__":
    s = ['h', 'e', 'l', 'l', 'o']
    reverse_string(s=s)
    print(s)