
import math
z = int(input("What is your number? "))
y = int(input("What is your 2nd number? "))
def factors(x, y):
  print("The factors of",x and y,"are")
  for i in range (1, x+1 ):
    if x%i == 0:
      print(i)
def factor(r):
  print("The factors of",r,"are")
  for i in range (1, r+1):
    if r%i == 0:
      print(i)

print("the gcd is", math.gcd(z,y))



