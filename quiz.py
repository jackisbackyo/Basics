print("Welcome to my quiz!")
playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
else:
    print("Then let's begin the quiz!")
    score = 0
answer = input("What does CPU stand for? ")
if answer.lower() == 'central processing unit':
    print("Correct!")
    score += 1
else:
    print("Wrong!")
answer = input("What does GPU stand for? ")
if answer.lower() == 'graphics processing unit':
    print("Correct!")
    score += 1
else:
    print("Wrong!")
answer = input("What does RAM stand for ? ")
if answer.lower() == 'random access memory':
    print("Correct!")
    score += 1
else:
    print("Wrong!")
answer = input("What does PSU stand for? ")
if answer.lower() == 'power supply unit':
    print("Correct!")
    score += 1
else:
    print("Wrong!")
answer = input("What does graphics card improve? ")
if answer.lower() == 'graphics':
    print("Correct!")
    score += 1
else:
    print("Wrong!")
answer = input("What is the the latest windows update? ")
if answer.lower() == 'windows 11':
    print("Correct!")
    score += 1
else:
    print("Wrong!")
answer = input("What does RAM give quick access to? ")
if answer.lower() == 'computing resources':
    print("Correct!")
    score += 1
else:
    print("Wrong!")
answer = input("Who was the 16th president of the U.S? (last name) ")
if answer.lower() == 'lincoln':
    print("Correct!")
    score += 1
else:
    print("Wrong!")
print("You got " + str(score) + " out of 8 questions correct!")
print("You scored " + str((score / 8) * 100) + "%")

