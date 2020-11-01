class A: 
	def __init__(self, a): 
		self.a = a 
	def __gt__(self, other): 
		if(self.a>other.a): 
			return True
		else: 
			return False
ob1 = input("Enter your CGPA:")
A(ob1) 
ob2 = input("Enter your friends CGPA:")
A(ob2) 
if(ob1>ob2): 
	print("Woah! You have a greater CGPA than your friend!") 
else: 
	print("Your friend has a greater CGPA then you!")