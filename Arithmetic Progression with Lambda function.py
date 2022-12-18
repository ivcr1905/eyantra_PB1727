# Import reduce module
from functools import reduce


# Function to generate the A.P. series
def generate_AP(a1, d, n):

    AP_series = []

    # Complete this function to return A.P. series
    for i in range(1,n+1):
        AP_series.append(a1+(i-1)*d)

    return AP_series


n=int(input("Enter the test cases:"))
for i in range(n):
    inli=input("Enter ap:").split()
    re=generate_AP(int(inli[0]),int(inli[1]),int(inli[2]))
    print(re)
    l=list(map(lambda x:x*x,re))
    print(l)
    sum1=reduce(lambda a,b:a+b,l)
    print(sum1)