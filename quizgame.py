# Welcome message
print("Welcome to my computer quiz!")

# Ask if the user wants to play and quit if they say no
playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()

# Start the quiz
print("Okay! Let's play :) ")

# Initialize score to 0
score = 0

# Ask the first question and check if the answer is correct
answer = input("What does the CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct')
    score += 1
else:
    print('Incorrect')

# Ask the second question and check if the answer is correct
answer = input("What does the GPU stand for? ")
if answer.lower() == "graphic processing unit":
    print('Correct')
    score += 1
else:
    print('Incorrect')

# Ask the third question and check if the answer is correct
answer = input("What does the RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct') 
    score += 1   
else:
    print('Incorrect')

# Ask the fourth question and check if the answer is correct
answer = input("What does the PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct')
    score += 1
else:
    print('Incorrect')

# Calculate and display the score
print("You got " + str(score) + " out of 4, with a total percentage of " + str((score/4) * 100) + "%")
