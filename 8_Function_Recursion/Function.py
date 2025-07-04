# def avg():#Function defination
#     num1 = int(input("Enter: "))
#     num2 = int(input("Enter: "))
#     num3 = int(input("Enter: "))
#     print((num1+num2+num3)/3)

# avg()#Function Call

#Function With argument
'''
def Show_Name(name):
    print(f"Hello {name}")

str = input("Enter your name:  ")
Show_Name(str)    
'''
#Default argument value
'''
def greet(name="stranger"):
    print("Hello ",name)

greet("tushar")

'''

#Recursion
'''
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

ans = fact(5)
print(ans)
'''

def total_sum(n):
    if(n==1):
        return 1
    else:
        return n+total_sum(n-1)
    
print(total_sum(100))    