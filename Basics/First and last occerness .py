n = int(input("Enter size: "))
arr = list(map(int, input("Enter elements: ").split()))
x = int(input("Enter element to find: "))

first = -1
last = -1

for i in range(n):
    if arr[i] == x:
        if first == -1:
            first = i
        last = i

print("First occurrence index:", first)
print("Last occurrence index:", last)