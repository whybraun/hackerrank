def swap_case(s):
    result = ''
    for letters in s:
        if letters.isupper() == True:
            result += letters.lower()
        elif letters.islower() == True:
            result += letters.upper()
        else:
            result += letters
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)