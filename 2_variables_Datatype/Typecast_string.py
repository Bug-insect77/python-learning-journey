# Type Casting Example

my_str = "10"
my_int = int(my_str)
print(my_str, my_int)
print(type(my_str), type(my_int))

# only strings that represent numbers can be converted to a float/int

my_invalid_str = "10a"
# This will cause an error:
# ValueError: invalid literal for int() with base 10: '10a'
# Uncommenting the below lines will raise an error

my_int2 = int(my_invalid_str)
print(my_invalid_str, my_int2)
print(type(my_invalid_str), type(my_int2))

my_str ="ABCD"
my_float_str = float(my_str)
print(my_str,my_float_str)
print(type(my_str),type(my_float_str))

my_str ="10"
my_float_str = float(my_str)
print(my_str,my_float_str)
print(type(my_str),type(my_float_str))


# Empty string to boolean
my_empty_str = ""
my_bool = bool(my_empty_str)
print(my_empty_str, my_bool)
print(type(my_empty_str), type(my_bool))
# Empty sting in Python = False 

