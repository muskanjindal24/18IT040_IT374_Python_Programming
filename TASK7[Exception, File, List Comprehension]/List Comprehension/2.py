class MyError(Exception): 
 pass
 
number = 100
try: 
  num = int(input("Enter a number: "))
  if num > number :
    raise(MyError(num)) 

except MyError: 
  print('More than 100 is not allowed !!!!')