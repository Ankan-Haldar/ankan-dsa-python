s = "a,b,e,e,e,e,r,r,f,f,t,u,h,n,f,d,s,e"
q = ["d", "a", "y", "x"]
# hashlist = [0] * 26

# # 1. Build the frequency array (O(N) time)
# for i in s:
#     if 'a' <= i <= 'z':  # Safety check: skip commas and spaces
#         index = ord(i) - 97
#         hashlist[index] += 1

# # 2. Query the counts (O(M) time)
# results = []
# for j in q:
#     index = ord(j) - 97
#     results.append(hashlist[index])

# print(results) # Output: [1, 1, 0, 0]





# Using dict{}

freq={}
for i in s:
    freq[i]=freq.get(i,0)+1
res=[freq.get(i,0) for i in q]
print(res)