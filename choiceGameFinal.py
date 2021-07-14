#Mays_Game
version = "v 1.0"

question1 = "The aliens have invaded.\nThey have promised to honor the alien code and grant you a wish if you tell them your friend's secret. Would you do it?\n(1)Of course,not!\n(2)Sorry,bestie. It was too tempting.\n"

question21 = "Noble choice! Sadly,your friend betrayed you! Now, you're on the run from the aliens. Will you:\n(1)Chase down your friend OR\n(2)Go into hiding?\n "

question22 = "Congrats! The aliens have offered you a rank on one condition: you have to capture your friend. Will you do it?\n(1)I have to\n(2)Not a chance\n"

question31 = "Your friend has been found! Things are awkward but you still have two choices.\n(1)Let bygones be bygones\n(2)Hand your friend in as tribute.\n"

question32 = "While on a supply run, you meet your friend. Will you:\n(1)forgive your friend OR\n(2)Hand your friend in as tribute?\n"

question33 = "The aliens are impressed. Hence, they offer you a chance.\n(1)Climb up their ranks.\n(2)Take over one of their franchising businesses.\n"

question34 = "OH NO. You both topped the wanted list. Will you:\n(1)join the human base camp OR\n(2)live in hiding with your friend?\n"

outcome45 = "You have been transferred to a different planet. Good luck in your galaxy fight!\n"

outcome46 = "The humans secretly plotted your death. You will be remembered...\n"

outcome47 = "Homo sapiens must prevail. An honor to have met you!\n"

outcome48 = "It turns out your friend was a spy! You are now a prisoner of war.\n"

def fight_back():
    print("The two of you decided to fight back together with people you found along the way. Human faction, good luck!\n")

def join_ranks():
    print("It turns out your friend is wanted for stealing supplies. The aliens have invited you to join their ranks. Hail, general!\n")



print("May's Game version 1.0\n")
x = input("Would you like to play a game? yes/no: ")
x = x.strip()

if x == "yes":
    playername = input("What is your name? ")
    print("")
    print("Mingalarbar,"+ playername+"!")
    print("")
    print("Type in 1 or 2 to continue.\n")
    answer1 = input(question1)

    if answer1 == "1":
        answer21 = input(question21)
        if answer21 == "1":
            answer31 = input(question31)
            if answer31 == "1":
                fight_back()
            elif answer31 == "2":
                join_ranks()
        elif answer21 == "2":
            answer32 = input(question32)
            if answer32 == "1":
                fight_back()
            elif answer32 == "2":
                join_ranks()

    elif answer1 == "2":
        answer22 = input(question22)
        if answer22 == "1":
            answer33 = input(question33)
            if answer33 == "1":
                print(outcome45)
            elif answer33 == "2":
                print(outcome46)
        elif answer22 == "2":
            answer34 = input(question34)
            if answer34 == "1":
                print(outcome47)
            elif answer34 == "2":
                print(outcome48)

elif x == "no":
    print("That's too bad, but have a great day!!")
else:
    print("(system error)\nPress (control/command + E) to restart.")