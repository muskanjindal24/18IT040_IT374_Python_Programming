import sys

n = int(sys.argv[1])

for i in range(1,11):
  print("{} x {} = {}".format(n,i,n*i))