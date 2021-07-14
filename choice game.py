#Mays_Game
version = "v 1.0"

question1 = "The aliens have invaded.\nThey have promised to honor the alien code and grant you a wish if you tell them your bestfriend's secret. Would you do it?\n(1)Of course,not!\n(2)Sorry,bestie. It was too tempting.\n"

question21 = "Noble choice! Sadly,your bestie betrayed you! Now, you're on the run from the aliens. Will you:\n(1)Team up with the aliens to chase down your friend OR\n(2)Hide from them?\n "

question22 = "Congrats! The aliens have offered you a rank on one condition: you have to kill your bestfried. What will you do?\n(1)Kill your bestie\n(2)Agree hesitantly with hope for the future.\n"

print("May's Game version 1.0\nMingalarbar !\n")
x = input("Would you like to play a game? yes/no: ")
x = x.strip()

if x == "yes":
    print("")
    print("Type in a number to continue.\n")
    answer1 = input(question1)
    if answer1 == "1":
        answer21 = input(question21)
        if answer21 == "1":
            print("okayy")
        elif answer21 == "2":
            print("okiee")
    elif answer1 == "2":
        answer22 = input(question22)
        if answer22 == "yes":
            print("okay too")

elif x == "no":
    print("That's too bad, but have a great day!!")
else:
    print("(system error)\nPress (control/command + E) to restart.")
