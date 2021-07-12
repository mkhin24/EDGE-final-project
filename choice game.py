#Mays_Game
version = "v 1.0"

print("Mingalarbar !")
choice = input("Would you like to play a game? yes/no: ")

if choice == "yes":
    print("")
    print("Type in a number to continue.\n")
    answer1 = input("The aliens have invaded.\nThey have promised to honor the alien code and grant you a wish if you tell them your bestfriend's secret. Would you do it?\n(1)Of course,not!\n(2)Sorry,bestie. It was too tempting.\n")
    if answer1 == "1":
        print("okay")
    elif answer1 == "2":
        print("okay up to here")
elif choice == "no":
    print("That's too bad, but have a great day!!")
else:
    print("(system error)\nPress (control/command + E) to restart.")