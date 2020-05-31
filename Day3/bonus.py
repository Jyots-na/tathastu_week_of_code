def bon(a,n):
    initial =1
    for i in range (0,n):
        if a[i]<= initial:
            initial =initial+a[i]
        else :
            break
    return initial
#main_program
a1=[1,2,3]
n1 = len(a1)
print(bon(a1,n1))
a2=[1,2,5,7]
n2=len(a2)
print(bon(a2,n2))
a3=[1,2,2,5,7]
n3= len(a3)
print(bon(a3,n3))
