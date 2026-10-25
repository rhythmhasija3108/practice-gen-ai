import pandas as pd

data ={
   "NAME":["Rahul","Priya","Aman","Neha","Rohan"],
   "Age":[21,22,20,23,21],
   "Marks":[85,67,92,45,76],
   "City":["Delhi","Mumbai","Delhi","Pune","Delhi"]

}

df=pd.DataFrame(data)
print(df)

#1-Display only the Marks column.
a=df["Marks"]
print(a)

#2-Display Name and Marks together.
b=df[["Marks","NAME"]]
print(b)

#Display Name , age , City
c=df[["NAME","Age","City"]]
print(c)