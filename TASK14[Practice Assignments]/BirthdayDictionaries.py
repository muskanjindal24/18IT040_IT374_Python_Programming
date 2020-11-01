import time
Birthdays ={
    "Mahendra Singh Dhoni": "7/6/1981",
    "Virat Kohli": "5/11/1988",
    "Rohit Sharma": "30/4/1987",
}
print("Welcome to the Birthday dictionary! We know the birthdays of:")
time.sleep(1)
for x in Birthdays:
    print(x)
    time.sleep(0.7)
choice= input("Who's birthday do you want to look up?")

if choice in Birthdays:
    print("{}'s birthday is {}.".format(choice,Birthdays[choice]))
else:
    print('{} is not in the list\n'.format(choice))