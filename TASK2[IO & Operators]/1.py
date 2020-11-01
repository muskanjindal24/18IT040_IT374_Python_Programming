def arith(A, B):
    print("Select an operator: ")
    print("+")
    print("-")
    print("*")
    print("/")
    print("%")
    print("//")
    print("**")
    while(True) :
      choice = input("Enter operator to use:")
      if choice == '+':
        print(A,"+",B,"=", A+B)
      elif choice == '-':
        print(A,"-",B,"=", A-B)
      elif choice == '*':
        print(A,"*",B,"=", A*B)
      elif choice == '/':
        print(A,"/",B,"=", A/B)
      elif choice == '%':
        print(A,"%",B,"=", A%B)
      elif choice == '//':
        print(A,"//",B,"=", A//B)
      elif choice == '**':
        print(A,"**",B,"=", A**B)
      else:
        print("Invalid input")
    

def assign(B):
    print("Select an operator: ")
    print("=")
    print("+=")
    print("-=")
    print("*=")
    print("/=")
    print("%=")
    print("**=")
    print("//=")
    A=1
    while(True) :
      choice = input("Enter operator to use:")
      if choice == '=':
        print(A,"=",B,"=", B)
      elif choice == '+=':
        print(A,"+=",B,"=", A+B)
      elif choice == '-=':
        print(A,"-=",B,"=", A-B)
      elif choice == '*=':
        print(A,"*=",B,"=", A*B)
      elif choice == '/=': 
        print(A,"/=",B,"=", A/B)
      elif choice == '%=':
        print(A,"%=",B,"=", A%B)
      elif choice == '//=':
        print(A,"//=",B,"=", A//B)
      elif choice == '**=':
        print(A,"**=",B,"=", A**B)
      else:
        print("Invalid input")

def comp(A, B):
    print("Select an operator: ")
    print("==")
    print("!=")
    print("<>")
    print(">")
    print("<")
    print(">=")
    print("<=")
    while(True) :
      choice = input("Enter operator to use:")
      if choice == '==':
        print(A,"==",B,"is", True if A == B else False)
      elif choice == '!=':
        print(A,"!=",B,"is", True if A != B else False)
      elif choice == '<>':
        print(A,"<>",B,"is", True if A != B else False)
      elif choice == '>':
        print(A,">",B,"is", True if A > B else False)
      elif choice == '<':
        print(A,"<",B,"is", True if A < B else False)
      elif choice == '>=':
        print(A,">=",B,"is", True if A >= B else False)
      elif choice == '<=':
        print(A,"<=",B,"is", True if A <= B else False)
      else:
        print("Invalid input")

def log(A, B):
    print("Select an Logical operator: ")
    print("and")
    print("or")
    print("not")
    while(True) :
      choice = input("Enter operator to use:")
      if choice == 'and':
        print(A,"and",B,"is", True if A and B else False)
      elif choice == 'or':
        print(A,"or",B,"is", True if A or B else False)
      elif choice == 'not':
        print(A,"not",B,"is", True if not(A and B) else False)
      else:
        print("Invalid input")

def bit(A, B):
    print("Select an operator: ")
    print("&")
    print("|")
    print("^")
    print("~")
    print("<<")
    print(">>")
    while(True) :
      choice = input("Enter operator to use:")
      if choice == '&':
        print(A,"&",B,"=", A & B)
      elif choice == '|':
        print(A,"|",B,"=", A|B)
      elif choice == '^':
        print(A,"^",B,"=", A^B)
      elif choice == '~':
        print("~",A,"=", ~A)
      elif choice == '<<':
        print(A,"<<","=", A<<2)
      elif choice == '>>':
        print(A,">>","=", A>>2)
      else:
        print("Invalid input")

def iden(A, B):
    print("Select an Logical operator: ")
    print("is")
    print("is not")
    while(True) :
      choice = input("Enter operator to use:")
      if choice == 'is':
        print(A,"is",B,"is", True if A is B else False)
      elif choice == 'is not':
        print(A,"is not",B,"is", True if A is not B else False)
      else:
        print("Invalid input")

def member(A):
    print("Select an Logical operator: ")
    print("in")
    print("not in")
    while(True) :
      B = [1,2,3,4,5,6,7,8,9]
      choice = input("Enter operator to use:")
      if choice == 'in':
        print(A,"in",B,"is", True if A in B else False)
      elif choice == 'not in':
        print(A,"not in",B,"is", True if A not in B else False)
      else:
        print("Invalid input")

print("Python Operator Calculator")
print("1. Arithmetic operators")
print("2. Assignment operators")
print("3. Comparison operators")
print("4. Logical operators")
print("5. Bitwise operators")
print("6. Identity operators")
print("7. Membership operators")

x = int(input("Enter the operators you want to use:"))

if x == 1:
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    arith(a,b)
elif x == 2:
  a = int(input("Enter a number: "))
  assign(a)
elif x ==3:
  a = input("Enter a number: ")
  b = input("Enter a number: ")
  comp(a,b)
elif x == 4:        
  a = input("Enter a number: ")
  b = input("Enter a number: ")
  log(a,b)
elif x == 5:
  a = int(input("Enter a number: "))
  b = int(input("Enter a number: "))
  bit(a,b)
elif x == 6:
  a = input("Enter a number: ")
  b = input("Enter a number: ")
  iden(a,b)
elif x == 7:
  a = input("Enter a number: ")
  member(a)
else:
  print("Enter valid choice")