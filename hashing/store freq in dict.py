nums=[1,2,0,1,3,4,2,3]
n=len(nums)
hashmap={}
for i in range(0,n):
    hashmap[nums[i]]=hashmap.get(nums[i],0)+1
print(hashmap)