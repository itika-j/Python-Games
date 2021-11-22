import random

movies = ['Kal Ho Naa Ho', 'Kabhi Alvida Naa Kehna','Dhoom', 'Partner, Om Shanti Om',
          'Kismat Konnection', 'Kambakkht Ishq' ,'Love Aaj Kal','Fanaa', 'Saawariya', 'Jodhaa Akbar',
          'Jab We Met', 'Singh Is Kinng', 'Rab Ne Bana Di Jodi', 'Love Aaj Kal', 'Dil Bole Hadippa',
          'Band Baaja Baaraat', 'Patiala House', 'Phillauri', 'Thande Koyle','Veer-Zaara']

movie = random.choice(movies).lower()
lost = False
print("Guess the characters")

guesses = [' ']

turns = 5

while turns > 0:

    failed = 0

    for char in movie:

        if char in guesses:
            print(char , end="")

        else:
            print("_" , end="")

            failed += 1


    if failed == 0:

        print("You Win")

        print("The movie is: ", movie)
        break

    choice = input("What to guess the movie.(y/n)")

    if choice == 'y':
        choiceMovie = input("Enter the movie: ").lower();
        if choiceMovie == movie:
            print("You Won!")
            break
        else:
            lost = True
            break

    guess = input("\n\nGuess a character: ")

    while len(guess)!=1:
        guess = input("Invalid Choice. Choose only one character: ")

    while guess in guesses:
        guess = input("You have already made that guess.\nChoose another Character: ")
        continue

    guesses += guess

    print("Your Guesses:", guesses[1:])

    if guess not in movie:

        turns -= 1

        print("Wrong")

        if turns == 0:
            print("You Loose")
            print("The movie name was:" + movie)
        else:
            print("You have", + turns, 'more guesses')

if lost == True:
    print("You Loose")
    print("The movie name was:" + movie)
    print("Score = 0")
else:
    print("Score", 20-len(guesses))