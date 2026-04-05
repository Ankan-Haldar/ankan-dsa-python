n=int(input("Enter n: "))

for i in range(1,n+1):
    for j in range(1,i+1):
        if j==i:
            print(i,end="")
        else:
            print(i,end="*")
    print()

for i in range(n,0,-1):
    for j in range(1,i+1):
        if j==i:
            print(i,end="")
        else:
            print(i,end="*")
    print()
    