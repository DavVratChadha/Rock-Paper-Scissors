#Rock-Paper-Scissors game by Dav Vrat Chadha

"""In this program, I have used "and" and "or" to makes the code shorter and better.
I have also used WHILE loop to continue the game till we want, and for best out of 5 rounds"""


import random
print("""Welcome to the Rock-Paper-Scissors Game, the perfect game to kill your boredom during lockdown.
Just like in Jumanji, you cannot leave this game and must play it.
You are playing against the computer and the fate of your planet is in your hands. Isn't that amazing?
Play well!! Best Of Three Rounds.""")
flag = 1
#flag is used to check if the user wants to play the game again
while flag == 1:
    win = 0
    i = 0
#while loop for game of 5 rounds
    while i < 5:
        print("\nRound " + str(i + 1)+ ".") #Printing round number
#Computer choice using random
        compChoice = random.randint(1,3)

#Turning computer's choice to words, so that we can print it to the console
        if compChoice == 1:
            compMove = "Rock"
        elif compChoice == 2:
            compMove = "Paper"
        else:
            compMove = "Scissors"
#Asking for User's choice
        userChoice = eval(input("""Choose from the following options(index):
(1) Rock
(2) Paper
(3) Scissors\n"""))

#Checking for tie
        if userChoice == compChoice:
            print("Computer also chose " + compMove + ".")
            print("""Its a Tie! Earth is still at risk!! How can you leave the fate of the planet hanging?
Let's do this round again.""")
#Checking if user has won the round
        elif (userChoice == 1 and compChoice == 3) or (userChoice == 2 and compChoice == 1) or (userChoice == 3 and compChoice == 2):
            print("Computer chose " + compMove + " and you beat it!")
            print("You win.")
            win += 1
            i += 1
#User lost the round
        else:
            print("Computer chose " + compMove + " and beat you!")
            print("You lose.")
            i +=1
#Checking for end of game
        if i > 2 and win > 2:
            print("\nCongratulations!! You have won the game. Earth is safe!!")
            break #used to end while loop
        elif (i == 5 and win < 3) or (i == 3 and win == 0):
            print("\nYou have lost the game. Earth will be destroyed but first, you will have to face the wrath of computers!!")
            break #used to end while loop

#Asking user if they want to play again
    flag = eval(input("""\nWould you like to play again?
Choose from the following options(index):
(1) Yes
(2) No\n"""))
    if flag == 2:
        print("\nThank you for playing this game.")
    print("***************************************************************************")
