n=int(input("Enter the value of n : "))
count=0
for i in range(1,n+1):
    divisor=0
    for j in range(1,i+1):
        if i%j==0:
            divisor+=1
    if divisor==9:
        count+=1
print("Number with exactly 9 divisor: ",count)