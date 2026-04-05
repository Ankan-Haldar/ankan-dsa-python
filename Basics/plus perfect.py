n=int(input("Enter the no: "))

temp=n
digitsum=0

while temp>0:
    digitsum+=temp%10
    temp//=10


root=int(n**0.5)

if digitsum==root and root*root==n:
    print("Plus perfect no")
else:
    print("not plus perfect")
