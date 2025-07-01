'''
n=10
while(n>0):
    print("Hello World",n)
    n-=1
'''
# Quick Quiz:  Write a program to print the content of a list using while loops.
'''
my_list = ["tushar","singh",1,2,3,4,"class"]
i =0
while(len(my_list)>i):
    print(my_list[i])
    i +=1
'''  
#using range funt 
'''
my_list = ["tushar","singh",1,2,3,4,"class"]
for i in range(0,len(my_list),1):
    print(my_list[i])
'''
#using for loop
'''
my_list = ["tushar","singh",1,2,3,4,"class"]

for i in my_list:
    print(i)
'''
#for loop with tuple 
'''                          
my_tuple = (1,2,3,4,56,"tushar_singh")
for it in my_tuple:
    print(it) 
'''
#for loop in string
'''   
my_string = "Tushar Singh"
for ch in my_string:
    print(ch)
else:
    print("DONE") #This will print when loop is exhausts!!
'''
