import random

string = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
len = 8
password = "".join(random.sample(string,len))
print("Generated Password:",password)