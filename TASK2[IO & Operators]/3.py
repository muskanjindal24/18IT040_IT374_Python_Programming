import sys
amt = int(sys.argv[1])
year = int(sys.argv[2])
rate = int(sys.argv[3])

CI = amt * pow((1+rate / 100),year)
print("Compand Interest = {}",CI)