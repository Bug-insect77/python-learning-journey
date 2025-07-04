# 1. Write a program using functions to find greatest of three numbers. 
'''
def maximun(num1,num2,num3):
    if(num1>num2 and num1>num3):
        return num1
    elif(num2>num1 and num2>num3):
        return num2
    else:
        return num3

a= int(input("Enter number: "))    
b= int(input("Enter number: "))    
c= int(input("Enter number: "))
print(maximun(a,b,c))    
'''

# 2. Write a python program using function to convert Celsius to Fahrenheit.
'''
def celtofah(num):
    return (num * (9/5)) + 32 

print(celtofah(40))
'''

# 3. How do you prevent a python print() function to print a new line at the end. 
#using end argument in the print function end=""
"""
print("tushar",end="")
print(" singh")

"""

# 4. Write a recursive function to calculate the sum of first n natural numbers. 
'''
def total_sum(n):
    if(n==1):
        return 1
    else:
        return n+total_sum(n-1)
    
print(total_sum(100)) 
'''

# 5. Write a python function to print first n lines of the following pattern: 
# *** 
# **               - for n = 3 
# * 
'''
 
def starprint(n):
    for i in range(n,0,-1):
       print("*"*(i))
   

starprint(3)
'''

# 6. Write a python function which converts inches to cms. 

'''
def intocm(n):
    return n*2.54
print(intocm(5.5))
'''
# 7. Write a python function to remove a given word from a list ad rip it at the same time. 

'''
def dosomething(word,list):
      n = []
      for i in list:
            if not(word == i):
                  n.append(i.strip(word))
      return n                 

n=dosomething("ar",["tushar","singh","bukhar","ar","one"])
print(n)
'''


# 8. Write a python function to print multiplication table of a given number

'''
def table(n):
    for i in range(1,n+1):
     print(f"{n} X {i} = {n*i}")
        
table(int(input("enter n: ")))
'''