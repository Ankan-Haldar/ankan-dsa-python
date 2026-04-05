class Solution:
    # Function to calculate factorial of a number.
    def factorial(self, n: int) -> int:
        # code here
        if n==0 or n==1:
            return 1
        return n* self.factorial(n-1)
# Taking user input
n = int(input("Enter a number: "))

# Creating object and calling function
obj = Solution()
result = obj.factorial(n)
print("Factorial:", result)