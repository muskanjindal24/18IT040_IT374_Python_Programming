import sys

n = (sys.argv[1])
sum_of_digits = 0
for digit in str(n):
  sum_of_digits += int(digit)

print("Sum of digits in {} is {}".format(n,sum_of_digits))

