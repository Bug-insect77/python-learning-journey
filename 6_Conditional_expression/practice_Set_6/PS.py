# 1. Write a program to find the greatest of four numbers entered by the user.
'''
my_list = []
my_list.append(int(input("Enter marks: ")))
my_list.append(int(input("Enter marks: ")))
my_list.append(int(input("Enter marks: ")))
my_list.append(int(input("Enter marks: ")))
print(my_list)
maxi = max(my_list)
print(maxi)
'''

# 2. Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.
'''    
My_marks = []

num1 =   int(input("Enter Marks: "))
num2 =   int(input("Enter Marks: "))
num3 =   int(input("Enter Marks: "))

my_average = ((num1+num2+num3)/300)*100

if(num1 >= 33 and num3>=33 and num2>=33 and my_average>40):
    print("You pass",my_average)
else:
    print("You fail",my_average)
'''
# 3. A spam comment is defined as a text containing following keywords: 
# "Make a lot of money", "buy now", "subscribe this", "click this". Write a program to detect these spams.
'''
p1= "Make a lot of money"
p2="buy now"
p3="subscribe this"
p4="click this"

sentence = input("Enter your Sentence: ")

if(p1 in sentence or p2 in sentence or p3 in sentence or p4 in sentence):
    print("Scammer")
else:
    print("NO Scam")
'''



# 4. Write a program to find whether a given username contains less than 10 characters or not.
'''
username = input("Enter your name: ")
if(len(username)<=10):
    print("10 nahi hai")
else:
    print("10 hai")    
'''
# 5. Write a program which finds out whether a given name is present in a list or not. 
'''
my_list = ["tushar","golu","molu","shamu","ramu"]

your_name = input("Enter name: ").lower()
print(your_name)
print(your_name in my_list)
'''
# 6. Write a program to calculate the grade of a student from his marks from the 
# following scheme: 
# 90 – 100 => Ex 
# 80 – 90 => A 
# 70 – 80 => B 
# 60 – 70  =>C 
# 50 – 60 => D 
# <50   => F 

'''    
# marks = []
# marks.append(int(input("enter your marks: ")))
# marks.append(int(input("enter your marks: ")))
# marks.append(int(input("enter your marks: ")))
# marks.append(int(input("enter your marks: ")))
# marks.append(int(input("enter your marks: ")))

total_marks = sum(marks)
marks_grade = total_marks/len(marks)
if(marks_grade >=90 and marks_grade <=100):
    print("EX")
elif(marks_grade >80 and marks_grade <=90):
    print("A")    
elif(marks_grade >70 and marks_grade <=80):
    print("B")    
elif(marks_grade >60 and marks_grade <=70):
    print("B")    
elif(marks_grade >50 and marks_grade <=60):
    print("D")
else:
    print("F")    
    '''
# 7. Write a program to find out whether a given post is talking about “Harry” or not

"""
post = input("Create Post: ")

if("Harry".lower() in post.lower()):
    print("Yes")
else:
    print("No")    
    """