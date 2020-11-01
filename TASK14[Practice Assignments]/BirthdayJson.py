import json
import time

birthday = {}
with open('birthdays.json', 'r') as f:
          birthday = json.load(f)

print("Welcome to the Birthday dictionary! We know the birthdays of:")
time.sleep(1)
for x in birthday:
    print(x)
    time.sleep(0.7)
choice= input("Who's birthday do you want to look up?")
if birthday[choice]:
    print('{} is born on {}\n'.format(choice, birthday[choice]))
else:
    print('{} is not in the list\n'.format(choice))