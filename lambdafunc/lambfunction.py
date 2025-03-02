#lambda function
a=float(input("enter a first no"))
b=float(input("enter a second no"))
x = lambda a, b: a if a > b else b
print(x(a,b))
