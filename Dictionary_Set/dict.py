# dict = {
#     "naam":"name",
#     "kaam":"Work",
#     "class":"kaksha"
# }

# # word = int(input("enter wor)d: ")

# print(dict.keys())

# s = {1,"2",2,3,4,5,6,7,8,9}
# print(s)

# s.discard(1)

# print(s)

# n =5
# while(n>0):
#     print(n)
#     n-=1
    

# n4 = int(input("Enter :"))

# if(n1>n2 and n1>n3 and n1>n4):
#     print(n1)
# if(n2>n1 and n2>n3 and n2>n4):
#     print(n2)
# if(n3>n2 and n3>n1 and n3>n4):
#     print(n3)
# if(n4>n1 and n4>n2 and n4>n3):
#     print(n4)

marks1 = int(input("Enter marks1 :"))
marks2 = int(input("Enter marks2 :"))
marks3 = int(input("Enter marks3 :"))

totalMarks = marks1 + marks2 + marks3
totalMarks_ = (totalMarks/300)*100


if(marks1>33):
    print("Pass in sub1:")
else:
    print("fail in sub1:")
if(marks2>33):
    print("Pass in sub2:")
else:
    print("fail in sub2:")
if(marks3>33):
    print("Pass in sub3:")
else:
    print("fail in sub3:")

print(totalMarks_)
print(totalMarks)

if(totalMarks_>40):
    print("pass in ALL")
else:
    print("Fails")    