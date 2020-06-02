size = int(input('Enter the no. of items you want to add in dictionary : '))
diction = dict()
for i in range(size):
    key = input("Enter the values for item "+ str(i+1)+ " in dictionary:")
    value = int(input("Enter the value for item "+ str(i+1)+" in dictionary : "))
    diction[key] = value 
result = dict()
for key,value in diction.items():
    if value not in result.values():
        result[key]=value
print('dictionary after removing duplicates :', result)
