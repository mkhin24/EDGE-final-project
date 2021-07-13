#Mays_Game
version = "v 1.0"

question1 = "The aliens have invaded.\nThey have promised to honor the alien code and grant you a wish if you tell them your bestfriend's secret. Would you do it?\n(1)Of course,not!\n(2)Sorry,bestie. It was too tempting.\n"

question21 = "Noble choice! Sadly,your bestie betrayed you! Now, you're on the run from the aliens. Will you:\n(1)Chase down your friend OR\n(2)Go into hiding and plan your next move ? "

question22 = "Congrats! The aliens have given you fringe benefits. Yet, they threatened you to keep on leaking secrets in exchange for your life. What will you do?\n(1)Call them out for cheating and fight.\n(2)Agree hesitantly with hope for the future."

print("May's Game version 1.0\nMingalarbar !")
choice = input("Would you like to play a game? yes/no: ")

if choice == "yes" or "YES" or "Yes":
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

elif choice == "no" or "NO" or "No":
    print("That's too bad, but have a great day!!")

else:
    print("(system error)\nPress (control/command + E) to restart.")
