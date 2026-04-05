n = int(input("Enter number: "))
temp=n
count=0

while temp>0:
    count+=1
    temp//=10

temp=n
sum=0

while temp>0:
    digit=temp%10

    power=1

    for i in range(count):
        power=power*digit

    sum+=power
    temp//=10

if sum==n:
    print("Amstrong no")
else:
    print("Not a amstrong no")