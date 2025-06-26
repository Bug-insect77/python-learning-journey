text = "  Hello World  "

print(text.lower())       # '  hello world  '
print(text.strip())       # 'Hello World'
print(text.replace("World", "Python"))  # '  Hello Python  '
print(text.find("World"))  # 8
print(text.split())       # ['Hello', 'World']
print("-".join(["a","b","c"]))  # 'a-b-c'
print(text.startswith("  He"))  # True
print(text.count("l"))  # 3
print((text.strip()).isalpha())  # False (contains spaces)


#Escape Squence Characaters
# \n , \t, \`, \\
print("aklsfaksja\nskaflkdfa")
print("aklsfaksja\tskaflkdfa")
print("aklsfaksja\'skaflkdfa")
print("aklsfaksja\\skaflkdfa")