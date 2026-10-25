a=[45,67,89,32,76,91,55,63,84,72]
print(a)
b = sum(a)
print("Sum of elements in the list:", b)
c = b/len(a)
print("Average of the list is :", c)
d =max(a)
print("Highest number in the list is:",d)
e=min(a)
print("Lowest number in the list is:",e)
#count greater than 70
count=0
for i in a:
    if i >= 70:
        count+=1
        print("Count greater than 70", count)  # here the code is in the loop , so it will print the count each time it finds a number greater than or equal to 70

#total count of numbers greater than or equal to 70
count=0
for i in a:
    if i >= 70:
        count+=1
print("Total count greater than 70:", count)      #here the code is outside the loop, so it will print the total count of numbers greater than or equal to 70 after checking all elements in the list

#students wo are failed
count =0
for i in a:
    if i<40:
        count+=1
print("Failed students:", count)

#print two number       