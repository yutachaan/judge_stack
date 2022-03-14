from linked_list import LinkedList

def is_match(s: str) -> bool:
    '''整合性判定'''

    linked_list = LinkedList()
    pair_brackets = {"(": ")", "{": "}", "[": "]"}

    for char in s:
        if char in list(pair_brackets.keys()):
            linked_list.push(char)
        elif char in list(pair_brackets.values()):
            try:
                left_brackets = linked_list.pop()
                if not(char == pair_brackets[left_brackets]):
                    return False
            except LinkedList.Empty:
                return False
    if linked_list.is_empty():
        return True
    else:
        return False

if __name__ == "__main__":
    s = input()
    if is_match(s): print("OK")
    else: print("NG")
