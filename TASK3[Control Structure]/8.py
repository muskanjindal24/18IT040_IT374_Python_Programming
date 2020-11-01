import sys

def Fibonacci(n): 
    f1 = 0
    f2 = 1
    if (n < 1): 
        return
    for x in range(0, n): 
        print(f2) 
        next = f1 + f2 
        f1 = f2 
        f2 = next
    print("\n")

n = int(sys.argv[1])  
print(Fibonacci(n))