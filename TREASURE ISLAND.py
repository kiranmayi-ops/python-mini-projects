print("Welcome to Treasure Island.Yout mission is to find the treasure")
way = input("left or right: ")
if(way == "left"):
    swim = input("swim or wait: ")
    if(swim == "wait"):
        Door = input("red or blue or yellow: ")
        if(Door == "yellow"):
            print("You win")
        elif Door == "red":
            print("game over")
        elif Door == "blue":
            print("game  over")
    else:
        print("game over")

else:
    print("game Over")
