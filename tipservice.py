y= input("Enter your bill:")
service= input("How was your sevice: ")
z=float(y)



if service == "bad":
    print(f'your total cost is: {z*0}')
elif service == "okay":
    print(f'your total cost is: {z*1.15}')
elif service == "good":
    print(f'your total cost is: {z*1.20}')
elif service == "great":
    print(f'your total cost is: {z*1.25}')



