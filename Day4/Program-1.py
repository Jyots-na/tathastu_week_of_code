size = int(input("Enter the size of tuple : "))
print("Enter the elements in tuple ")
a =[]
for i in range(size):
    a.append(input())
a = tuple(a)
elements = input("Enter the element whose occurrance you want to know: ")
print("Tuple contains the element",a.count(elements),"times")
