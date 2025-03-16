#3. ⁠Write a function validate_list(lst) that asserts the list must not be empty.
def validate_list(list):
    assert len(list) > 0, "The list must not be empty!"
    print("The list is valid.")

try:
    my_list = [1,2,3]
    validate_list(my_list)

except AssertionError as e:
    print(f"Error: e")
    