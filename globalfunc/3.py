#3 Maintain a Global List of Names
#Define a global list names and write functions to:


names = []
def add_name(name):
    global names  
    names.append(name)
    print(f"{name} Added to the list.")

def remove_name(name):
    global names  
    if name in names:
        names.remove(name)
        print("remove")
    else:
        print("not found")

def display_names():
    global names  
    print("Names in the list:")
    for name in names:
        print(name)
add_name("abi")
add_name("Bob")
display_names()
remove_name("abi")
display_names() 
