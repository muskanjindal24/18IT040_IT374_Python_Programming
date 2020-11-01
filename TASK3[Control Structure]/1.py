import sys

x1 = int(sys.argv[1])
x2 = int(sys.argv[2])
x = {x1,x2}

for i in x:
  if(i%3==0 and i%5==0):
    print("{} is divisible by 3 and multiple of 5".format(i))
  else:
    print("{} is not divisible by 3 and multiple of 5".format(i))