n=int(input())
for i in range(n):
     a=int(input("Enter the number:"))
     result=[]
     b=[]
     
     for i in range(a):
         
         b.append(i)
     #conditions
     for i in b:
         if (i==0):
             result.append(i+3)
         elif(i%2==0):
             result.append(i*2)
         else:
             result.append(i*i)
     print("This is b:",b)
     print("Result:",result)             
#Need to do the printing part.     