n=int(input("Enter the loop:"))
for i in range(n):
    a=int(input("Enter number:"))
    for i in range(a,0,-1):
       for j in range(1,i+1):
           if (j%5==0):
               print('#',end='')
           else:
               print('*',end='')
           
       print()    