def get_salary_details(b):
  DA = b * 0.7
  MA = 100
  TA = 400
  TOTAL_SALARY = b + DA + MA +TA
  print("DA = {}, MA = {}, TA = {}, TOTAL_SALARY = {}".format(DA,MA,TA,TOTAL_SALARY))

x = float(input("Enter basic salary:"))
get_salary_details(x)