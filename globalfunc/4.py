
#4Create a program with two global variables, a and b. Write a function that swaps their values using the global keyword and prints the updated values.

a,b=5,10
def swap():
    global a,b
    a,b=b,a
    print("after swapping",a,b)
swap()

