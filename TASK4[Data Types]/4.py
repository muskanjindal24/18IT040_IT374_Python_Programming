def CountList(list): 
    freq = {} 
    for item in list: 
        if (item in freq): 
            freq[item] += 1
        else: 
            freq[item] = 1
    for key, value in freq.items(): 
        print ("% d : % d"%(key, value)) 

def CountTuple(tup): 
    count = 0
    freq = {}
    for ele in tup: 
        if (ele in freq): 
            freq[ele] += 1
        else: 
            freq[ele] = 1
    for ele, count in freq.items(): 
        print ("% d : % d"%(ele, count))

def Countdic(dic): 
    freq = {} 
    for item in dic.values(): 
        if (item in freq): 
            freq[item] += 1
        else: 
            freq[item] = 1
    for key, value in freq.items(): 
        print ("% d : % d"%(key, value))

if __name__ == "__main__":  
    mylist =[1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2]
    print("Given list:",mylist)
    CountList(mylist)
    tup = (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2) 
    print("Given tuple:",tup)
    CountTuple(tup)
    dic = {'a': 7, 'b': 8, 'c':9, 'd':7, 'e':8} 
    print("Given dictionary:",dic)
    Countdic(dic)
