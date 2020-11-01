list1 = [1,3,4,9,0,2,4,4,5,9]
list2 = [2,4,6,8,0,2,8]
listoverlap = [x for x in list1 for y in list2 if x == y]
print (set(listoverlap))