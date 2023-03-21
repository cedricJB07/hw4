def palindrome(list):
    num = len(list)
    for i in range (num // 2):
        if list[i] != list[num - i - 1]:
            return False
    return True