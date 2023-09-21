if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    a = tuple(integer_list)

    t = hash(a)

    print(t)