#2 Track Total Sum Using a Global Variable
#Create a function that takes a number as input and adds it to a global variable total_sum. Print the updated total_sum after each function call.

total_sum=0
def add(num):
    global total_sum 
    total_sum+= num
    print("total_sum", total_sum)
add(10)
add(20)
add(30)
