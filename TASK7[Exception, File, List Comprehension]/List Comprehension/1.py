import sys

n = int(sys.argv[1])
fibonacci_list = [0,1]
[fibonacci_list.append(fibonacci_list[k-1]+fibonacci_list[k-2]) for k in range(2,n)]

if n<=0:
   print('+ve numbers only')
elif n == 1:
   fibonacci_list = [fibonacci_list[0]]
   print(fibonacci_list)
else:
   print(fibonacci_list)