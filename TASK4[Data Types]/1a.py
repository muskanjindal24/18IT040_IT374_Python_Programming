def check(dict, key): 
      
    if key in dict.keys(): 
        print("Yes, given key is present with a value of",dict[key]) 
    else: 
        print("The given key is not present") 
  
# Driver Code 
dict = {'a': 100, 'b':200, 'c':300} 

key = input("Enter a key: ")
check(dict, key) 