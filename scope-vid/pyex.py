
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

if __name__ == "__main__":
    my_fib = [fibonacci(i) for i in range(10)]
    header ="|\tn\t|\t#Fibo\t|"
    print("-"*(len(header) + 4*5)) 
    print(header)
    print("-"*(len(header) + 4*5)) 
    for i, num in enumerate(my_fib):
        print(
            f'|\t{i}\t|\t{num}\t|'
        )