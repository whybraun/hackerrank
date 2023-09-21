#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    result = f'Hello {first} {last}! You just delved into python.'
    return print(result)

if __name__ == '__main__':
    first = str(input())
    last = str(input())
    print_full_name(first, last)
