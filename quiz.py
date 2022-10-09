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
answer = input("What does NGNL stand for? ")
if answer.lower() == 'no game no life':
    print("Correct!")
    score += 1
else:
    print("Wrong!")
answer = input("What is the name of sun wukong's staff? ")
if answer.lower() == 'ruyi jingu ban':
    print("Correct!")
    score += 1
else:
    print("Wrong!")
answer = input("What is Goku's saiyan name? ")
if answer.lower() == 'kakkarot':
    print("Correct!")
    score += 1
else:
    print("Wrong!")
answer = input("When is Bennet's Birthday? (Genshin Impact) ")
if answer.lower() == '2/28':
    print("Correct!")
    score += 1
else:
    print("Wrong!")
print("You got " + str(score) + " out of 8 questions correct!")
print("You scored " + str((score / 8) * 100) + "%")

