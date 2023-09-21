def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1, number + 1):
        decimal = str(i)
        octal = oct(i)[2:]
        hexadecimal = hex(i)[2:].upper()
        binary = bin(i)[2:]
        print("{:>{width}} {:>{width}} {:>{width}} {:>{width}}".format(decimal, octal, hexadecimal, binary, width=width))

if __name__ == '__main__':
    n = int(input("Введите число: "))
    print_formatted(n)
