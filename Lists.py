if __name__ == '__main__':
    N = int(input())

    data = []

    for _ in range(N):
        command = input().split()

        if command[0] == "insert":
            i = int(command[1])
            e = int(command[2])
            data.insert(i, e)
        elif command[0] == "print":
            print(data)
        elif command[0] == "remove":
            e = int(command[1])
            data.remove(e)
        elif command[0] == "append":
            e = int(command[1])
            data.append(e)
        elif command[0] == "sort":
            data.sort()
        elif command[0] == "pop":
            data.pop()
        elif command[0] == "reverse":
            data.reverse()
        else:
            break
