# 1. Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.
'''
f = open("poem.txt")
text = f.read()
if("twinkle" in text):
    print("present")
else:
    print("Not present")

f.close()

'''
# 2. The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score. 
'''
import random

def game():
    print("you are Playing the game")
    score = random.randint(1,101)
    print(f'Your score {score}')
    with open("highscore.txt") as f:
       highscore = f.read()
       if(highscore==""):
           highscore=0
    if(int(highscore)<score):
        with open("highscore.txt","w") as f:
            f.write(str(score))
               
game()

'''


# 3. Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13 – year old. 

'''
def table(n):
     with open(f"tables/table_{n}.txt","w") as f:
       for i in range (1,11):
        f.write(f"{n}*{i}= {n*i}\n")        

for i in range (1,21):
    table(i)

'''

# 4. A file contains a word “Donkey” multiple times. You need to write a program which replace this word with ##### by updating the same file.  

'''
with open("file.txt") as f:
    content = f.read()
    newcontent = content.replace("Donkey","#######")
with open("file.txt","w") as f:
    f.write(newcontent)    

'''
# 5. Repeat program 4 for a list of such words to be censored. 
'''

words = ["Donkey","bad","ganda","dirty"]
with open("file.txt") as f:
    content = f.read()
    for word in words:
      content = content.replace(word,"#"*len(word))
      with open("file.txt","w") as f:
       f.write(content)    
'''

# 6. Write a program to mine a log file and find out whether it contains ‘python’.
'''
with open("log.txt") as f:
    content = f.read()
    if("python" in content):
        print("Present")
    else:
        print("not Present")    
'''


# 7. Write a program to find out the line number where python is present from ques 6. 

'''    
with open("log.txt") as f:
    lines = f.readlines()
lineno=1
for line in lines:
    print(lines)
    if("python" in line):
     print(f"Present at line: {lineno}")
     break 
    lineno +=1
else:
     print("not Present")    

'''
# 8. Write a program to make a copy of a text file “this. txt” 
'''
with open("this.txt") as f:
    content = f.read()
with open("copy_this.txt","w")as f:
    f.write(content)
'''


# 9. Write a program to find out whether a file is identical & matches the content of another file.
'''   
with open("this.txt") as f:
    content = f.read()
with open("log.txt")as f:
    content2 = f.read()
if(content == content2):
    print("Identical")
else:
    print("NOT identical") 
'''


# 10. Write a program to wipe out the content of a file using python. 
'''
import os
with open("copy_this.txt","w") as f:
     f.write("")
if os.path.exists("copy_this.txt"):
  os.remove("copy_this.txt")
else:
    print("file not exist")
'''

# 11. Write a python program to rename a file to “renamed_by_ python.txt.
'''
for renaming file you have to create a copy of that file by name renamed_by_python 
and delete the original file using the os module





import os
with open("copy_this.txt","w") as f:
     f.write("")
if os.path.exists("copy_this.txt"):
  os.remove("copy_this.txt")
else:
    print("file not exist")
'''