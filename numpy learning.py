import numpy as np
marks = np.array([45,67,89,32,76,91,55,63,84,72])
#average
a=np.average(marks)
print("average",a)
#maximum
b=np.max(marks)
print("maximum",b)
#minimum
c=np.min(marks)
print("minimum",c)
#total
d=np.sum(marks)
print("sum",d)
#Total sum of marks of student scored >=70  
e=np.sum(marks[marks>=70])
print(e)

#total student scored >=70
f=np.sum(marks>70)
print(f)

# All marks that are 70 or above
g=marks[marks>70]
print(g)

#All marks that are below 40
h=marks[marks<40]
print(h)

#The average of only the students who scored 70+
i=np.average(marks[marks>70])
print(i)


# Average of all students
a=np.average(marks)
print("average",a)

# Average of students who scored 70 or above
g=marks[marks>70]
print(g)

# Highest mark among students who scored 70 or above
j=np.max(marks[marks>70])
print(j)

# How many students scored below the average
a=np.average(marks)
count=np.sum(marks<a)
print(count)


# Create a new array containing only marks between 50 and 80, inclusive
k=marks[(marks>50)&(marks<80)]
print(k)

