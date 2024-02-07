
y = int(input("What is your number? "))


def factors(x):
  print("The gcf of",x,"are")
  for i in range (1, x+1):
    if x%i == 0:
      print(i)



factors(y)

