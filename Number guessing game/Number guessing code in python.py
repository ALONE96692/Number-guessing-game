import random 
mistakes = 0
secret_number = random.randint(1,1000)


while True:
    num = int(input("Guess the number"))
    if num == secret_number:
        print ("Correct Guess")
        break
    else:
        print ("Wrong Guess")
        mistakes = mistakes + 1
    if mistakes >= 3:
        if num > secret_number:
            print ("HINT - Guess lower!")
        elif num < secret_number:
            print("HINT - Guess higher")
