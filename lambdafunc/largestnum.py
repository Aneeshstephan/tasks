
#largest num
a=int(input("enter a first no"))
b=int(input("enter a second no"))
c=int(input("enter a third no"))
largest_of_three = lambda a, b, c: max(a, b, c)
largest_number = largest_of_three(a,b,c)
print(largest_number)