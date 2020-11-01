def Remove(sets,st): 
    sets.remove(st) 
    print("Modified set:",sets) 

sets = set(["Web", "CN", "DBMS", "DSA", "AWT"])
print("Given set:",sets)
st = input("Enter item you want to remove: ")
Remove(sets,st)
