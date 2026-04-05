def countdown(n):
    # 1. Base Case: Stop when we hit 0
    if n == 0:
        print("Blast off!")
        return 
    
    # 2. Action: Print the current number
    print(n)
    
    # 3. Recursive Step: Call the function again with n-1
    countdown(n - 1)

countdown(5)
