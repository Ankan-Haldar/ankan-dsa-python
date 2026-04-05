n=[1,2,3,10,9,5,3,5,2,5,8,7]
m=[11,3,4,5,2,67,111]

# hashlist=[0]*11
# for i in n:
#     hashlist[i]+=1
# for j in m:
#     if j<0 or j>10:
#         print(0)
#     else:
#         print(hashlist[j]) 



# same solution using {}

freqmap={}
for i in n:
    freqmap[i]=freqmap.get(i,0)+1
res=[]
for j in m:
    if j in freqmap:
        count=freqmap.get(j,0)
        res.append(count)
print(f"Frequencies of m in n: {res}")