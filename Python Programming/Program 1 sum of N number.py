number=int(input("Enter a number: "))
if number<=0:
    print("Enter a positive number.")
else:
    sum=0
    while(number>0):
        sum+=number
        number-=1
    print(f"The Summation is: {sum}")