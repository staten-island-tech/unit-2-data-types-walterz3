

z = int(input("What is your number? "))
y = int(input("What is your 2nd number? "))
factor_list=[]
def factors(x, y):
  for i in range (1, x+1, y+1):
    if x%i == 0 and y%i == 0:
      factor_list.append(i)


print(factor_list[-1])
""" (f"The factors of"z"and"y"is"(factor_list[-1])) """