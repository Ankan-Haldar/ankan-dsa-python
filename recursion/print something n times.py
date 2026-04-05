n=int(input("Enter the value of n : "))
x="Ankan"
def question1(x,n):
    if n==0:
        return
    print(x)
    question1(x,n-1)
question1(x,n)