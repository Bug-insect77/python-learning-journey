# name = input("Enter your name")

# print("good mor ning "+name)
# print(f"good mor ning {name}") 
# # f string

letter = '''   Dear <|Name|>, 
You       are      selected! 
<|Date|'''

print(letter.replace("Dear <|Name|>","Tushar").replace("<|Date|","20-02-02").strip())