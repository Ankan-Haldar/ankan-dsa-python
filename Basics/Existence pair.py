n=int(input("Enter n: "))


arr=list(map(int,input("Enter array elements: ").split()))

target=int(input("Enter Target"))

s=set()

for i in arr:
    if(target-i) in s:
        print(f'print pair found {i} {target-i}')
        break
    s.add(i)
else:
    print("No pair exist")