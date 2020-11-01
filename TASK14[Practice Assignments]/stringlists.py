string = input("Enter a string:")
if string[::-1] == string[0:]:
    print(string, " is a palindrome")
else:
    print(string, " is not a palindrome")