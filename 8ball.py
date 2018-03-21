# Import the modules
import sys
import random

ans = True

while ans:
    question=input("Ask the magic 8 ball a question: (press enter to quit) ")
    
    answers = random.randint(1,8)
    
    if question == "":
        sys.exit()
    
    elif answers == 1:

       print('d')
    
    elif answers == 2:
        print('d2')
    
    elif answers == 3:
        print('d3')
    
    elif answers == 4:
        print('d4')
    
    elif answers == 5:
        print('d5')
    
    elif answers == 6:
        print('d6')
    
    elif answers == 7:
        print('d7')
    
    elif answers == 8:
        print('d8')