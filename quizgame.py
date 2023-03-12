print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :) ")
score = 0

answer = input("What does the CPU stands for? ")
if answer.lower() == "central processing unit":
    print('Correct')
    score += 1
else:
    print('Incorrect')
    
answer = input("What does the GPU stands for? ")
if answer.lower() == "graphic processing unit":
    print('Correct')
    score += 1
else:
    print('Incorrect')

answer = input("What does the RAM stands for? ")
if answer.lower() == "read only memory":
    print('Correct') 
    score += 1   
else:
    print('Incorrect')

answer = input("What does the PSU stands for? ")
if answer.lower() == "power supply":
    print('Correct')
    score += 1
else:
    print('Incorrect')
    
print("You got " + str(score) + " with a total percent of "  + str((score/ 4) * 100) + "%")
