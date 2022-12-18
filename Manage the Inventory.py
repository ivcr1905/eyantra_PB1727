a={}
n=int(input("Enter the number:"))
for i in range(n):
    a1=int(input("Enter number inventories items:"))
    
    for i in range(a1):
        l1=input("Enter:")
        l1=l1.split()
        a[l1[0]]=int(l1[1])
        print("Dictionary:",a)
    b1=int(input("Enter number queries:"))
    for i in range(b1):
        l1=input("Enter query:")
        l1=l1.split()
        if (l1[0]=="ADD"):#add funtion..
            if (l1[1] not in a.keys()):
                l1[2]=int(l1[2])
                l1.remove("ADD")
                a.update(dict([l1]))
                print("Dictionary:",a)
            else:
                 l1[2]=int(l1[2])
                 a[l1[1]]=l1[2]+a[l1[1]]
                 print("Dictionary:",a)
        if (l1[0]=="DELETE"):#DElete funtion...
           #l1.remove("DELETE")
            if (l1[1] in a.keys()):
                if (a[l1[1]]==l1[2]):
                    a.pop(l1[1])
                    print(a)
                else:
                    l1.remove("DELETE")
                    a.update(dict([l1]))
                    print(a)
            