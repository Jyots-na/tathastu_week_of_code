size = int(input("enter the no. of wwords you wanna add in the dictionary : "))
dict =[]
for i in range(size):
    dict.append(input("enter the word "+ str(i+1) + ":"))
size = int(input("Enter the no. of character you want to add in array: "))
arr =[]
result =[]
print("enter the characters in array one by one ")
for i in range(size):
    arr.append(input())
for word in dict:
    if set(word).issubset(set(arr)):
        result.append(word)
print(" , " .join(result) + " . ")
