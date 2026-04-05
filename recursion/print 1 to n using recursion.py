i=int(input("i: "))
n=int(input("n: "))

# Using head recursion
# def func(i,n):
#     if i>n:
#         return 
#     print(i)
#     func(i+1,n)
# func(i,n)



# Using tail recursion

# def func(i,n):
#     if i>n:
#         return
#     func(i+1,n) 
#     print(i)
# func(i,n)
# output: 3 2 1



# required 1 2 3 4 5

# def func(n):
#      if n==0:
#          return
#      func(n-1) 
#      print(n)
# func(n)