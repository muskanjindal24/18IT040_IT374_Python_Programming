def make_multiplier_of(limit=10):
  def multiplier(x):
    for i in range(1,limit+1):
      print(x*i, end =" "),  
  return multiplier

table_of = make_multiplier_of() 
print(table_of(3))
table_of = make_multiplier_of(5)
print(table_of(4))
