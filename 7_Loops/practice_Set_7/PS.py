#  1. Write a program to print multiplication table of a given number using for loop. 
'''
num = int(input("Enter Number: "))
for i in range(1,11):
    print(num*i)
else:
    print("Completed")    
'''


# 2. Write a program to greet all the person names stored in a list ‘l’ and which starts with S. 
'''
l = ["Harry", "Soham", "Sachin", "Rahul"] 
for name in l:
    if(name.startswith("S")):
        print(f'hello {name}')
'''
'''
for item in l:
    if(item[0]=='S'):
        print(f'Hello {item}, How are you?')
    else:
        print(item)    
'''

# 3. Attempt problem 1 using while loop. 
'''
num = int(input("Enter Number: "))
i=1
while(i<11):
    print(i*num)
    i+=1
'''


# 4. Write a program to find whether a given number is prime or not.
'''
num = int(input("Enter Number: "))
if(num==1):
    print("Not Prime")
else:    
 temp =0
 for i in range(2,num,1):
    if(num%i==0):
        temp +=1

 if(temp==0):
    print("Prime")
 else:
    print("Not Prime")    
'''

# 5. Write a program to find the sum of first n natural numbers using while loop. 
#M-1
'''
n = int(input("Enter N: "))
sum = n*(n+1)/2
#M-2
sum2=0
for i in range(1,n+1):
    sum2+=i
    i+=1

print(int(sum),sum2)
'''
# 6. Write a program to calculate the factorial of a given number using for loop. 
'''
n = int(input("Enter N: "))
fact =1
for i in range(1,n+1,1):
    fact *=i
    i+=1
else:
    print(fact)
'''

# 7. Write a program to print the following star pattern. 
#    * 
#   *** 
#  *****  for n = 3
 
'''
n = int(input("Enter N: "))
for i in range(n+1):
    print(" "* (n-i), end="")
    print("*" *(2*i-1),end=""
          )
    print("")

    
'''


# 8. Write a program to print the following star pattern: 
# * 
# ** 
# ***      for n = 3 
'''
n = int(input("Enter N: "))

for i in range(1,n+1):
    print("*" *n,end="")
    print("")
'''


# 9. Write a program to print the following star pattern. 
# * * * 
# *   *    for n = 3 
# * * * 

'''
n = int(input("Enter N: "))
for i in range(1,n+1):
    if(i==1 or i==n):
        print("* "*n,end="")
    else:
        print("* ",end="")
        print("  "*(n-2),end="")    
        print("* ",end="")
    print("")    
'''

# 10. Write a program to print multiplication table of n using for loops in reversed 
# order.
'''
n = int(input("Enter N: "))
for i in range(10,0,-1):
   print(f"{n} X {11-i } == {n*(11-i)}")

'''    


