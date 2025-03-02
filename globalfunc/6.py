#6Create a function call_me() that keeps track of how many times it has been called using a global variable count.
counter=0
def call_me():
    global counter
    counter+=1
    print(counter)
call_me()    
call_me()