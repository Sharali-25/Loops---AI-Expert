num=int(input("Enter the number : "))
temp=num
sum=0
while temp>0:
    digit=temp%10
    sum=sum+digit**3
    temp=temp//10
if sum==num:
    print("Its an Armstrong Number")
else:
    print("Its not An Armstrong Number")