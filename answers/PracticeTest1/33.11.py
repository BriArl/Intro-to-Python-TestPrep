def fibonacci(n):
    if n < 0:
        return -1
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    
    for _ in range(2, n + 1):
        c = a + b
        a = b
        b = c
    
    return b


if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')