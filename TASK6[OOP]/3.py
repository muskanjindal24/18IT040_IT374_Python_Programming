class meter():  
    def show(self,cm): 
      meter = cm / 100.0; 
      print("Length in meter = " , 
               meter , "m");

class kilo():  
    def show(self,cm):
      kilometer = cm / 100000.0;  
      print("Length in Kilometer = ",  
             kilometer , "km");  

class centi(meter,kilo):  
    def show(self,cm): 
      print("Length in centimeter = ",  
             cm , "cm");           
   
cm = int(input("Enter value in centimeter:"))
g = centi() 
h = kilo()
i = meter()
g.show(cm) 
h.show(cm) 
i.show(cm) 


