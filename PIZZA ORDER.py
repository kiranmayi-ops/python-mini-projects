print("Welcome to python pizza Delivery")
size = input("What size pizza do you want?S ,M or L: ")
pepperoni = input("Do you want pepperoni on your pizza?Y or N: ")
cheese = input("Do ypu want extra cheese?Y or N: ")
bill = 0
if size == "S":
    bill = bill+15
elif size == "M":
    bill = bill+20
elif size == "L":
    bill = bill+25
else:
        print("you typed wrong")
if pepperoni == "Y":
    if size == "S":
        bill = bill+2
else:
    bill = bill+3 
if cheese == "Y":
    bill = bill+1
    print(f"Your bill is: ${bill}")
