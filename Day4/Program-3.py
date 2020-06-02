size = int(input("Enter the no. of items you want to add in Dictionary : "))
diction = dict()
for i in range(size):
    key = input("Enter the value for item " + str(i+1) + " in dictionary: ")
    value = int(input("Enter the value for item  "+ str(i+1)+ " in dictionary: "))
    diction[key]= value
print("The third largest value in the dictionary is",list(sorted(diction.values()))[-2])
