#variable naming
#As a good practice, you should avoid using names like str, bool, float, etc. because they override Python's built-in types and functions

my_str = "string"
my_num = 5
my_bool = True
my_float = 5.55
my_nothing = None

print(my_str, f"Type of {my_str}", type(my_str))
# this is called an f-string: print(f"{variable}")

print(my_num, f"Type of {my_num}", type(my_num))
print(my_bool, f"Type of {my_bool}", type(my_bool))
print(my_float, f"Type of {my_float}", type(my_float))
print(my_nothing, f"Type of {my_nothing}", type(my_nothing))


# use for single line comment
""" - multiline comment """
''' - multiline comment '''

input("enter value")
#This function allows the user to take input from the keyboard as a string.