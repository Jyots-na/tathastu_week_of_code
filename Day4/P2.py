sizeL = int(input("Enter the no. of tuples you want to add in the list: "))
sizeT = int(input("Enter the no. of elements you want to add in each tuple: "))
List =[]
for i in range(sizeL):
    print("enter thr elements in Tuple", i+1)
    Tuple=[]
    for j in range(sizeT):
        Tuple.append(int(input("Enter the element" + str(j+1) +": ")))
    List.append(tuple(Tuple))    
n = int(input("Enter the nth index about which you want to sort the list : "))
List.sort(key = lambda x : x[n])
print("After sorting list will be : ",List)
