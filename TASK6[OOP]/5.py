from datetime import date 
class check: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 

    @classmethod
    def BirthYear(cls, name, year): 
        return cls(name, date.today().year - year) 
       
    @staticmethod
    def Adult(age): 
        return age > 18
  
actualAge = check('Muskan', 20) 
ByBirthYear = check.BirthYear('Muskan', 2000) 
  
print("Age of Muskan:",actualAge.age) 
print("Muskan was born in 2000, so his age is:",ByBirthYear.age) 
print("Muskan is an adult?",check.Adult(20))