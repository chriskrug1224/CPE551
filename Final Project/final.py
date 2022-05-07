import random
#set up
print("Hi! Welcome to the guessing number game \n")
while(True): #Check if input is an integer
    max = (input("Please enter the highest integer number you would like to guess up to (must be a positive number!)\n"))
    if (max.isnumeric()):
        max = int(max)
        if (max > 1):
            break
        else:
            print("Please enter an integer greater than 1")
        
    else:
        print("Please only enter integer numbers, not strings or decimals!")
        
sol = random.randint(1,max) #Randomly Selected Solution
counter = 0

print("What do you think the number is? :) hint: it is 1 to " + str(max))

#logic
run = True
while (run):
    userInput = int(input("Please guess now : "))
    if userInput == sol: #Correct Answer
        print("Great job! The answer was " + str(sol) + "!")
        counter +=1
        if counter <=1:
            print("Wow! And it only took you " + str(counter) + " try!")
        else:
            print("Not bad! Only took you " + str(counter) + " attempts to get it!")
        run = False #End Game
    elif userInput < sol: #Lower Than Answer
        print("Too small! Try a higher number")
        counter +=1
        continue
    else: #Higher Than Answer
        print("Too big! Try a smaller number")
        counter +=1
        continue
    
            
