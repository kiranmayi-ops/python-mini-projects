import random
user_choice=int(input("What do you choose?Type 0 for Rock,1 for Paper,2 for Scissors"))
computer_choice=random.randint(0,2)
print(f"Computer Choice{computer_choice}")
if user_choice>=3 or user_choice<0:
    print("you typed an invalid number.You loss")    
elif user_choice==0 and computer_choice==2:
    print("you win")
elif user_choice==2 and computer_choice==0:
    print("you lose")    
elif(computer_choice>user_choice):
    print("you lose")
elif user_choice>computer_choice:
    print("you win")    
elif computer_choice == user_choice:
    print("It's a draw")    
elif user_choice>=3 or user_choice<0:
    print("you typed an invalid number.You loss")    