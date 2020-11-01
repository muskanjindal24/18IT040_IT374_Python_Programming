def function(x):
    return list(set(x))

given_list = [1,2,3,4,5,1,2,3,4,5,6]
print("Given list:")
print(given_list)
print("List after removing the duplicates:")
print(function(given_list))