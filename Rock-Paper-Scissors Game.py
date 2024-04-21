import random

while True:
    user=input("Enter a choice Rock,Paper,Scissors:")
    pactions=["Rock","Paper","Scissors"]  #possible acction
    computers=random.choice(pactions) #computer action
    print(f"You chose={user},\ncomputers chose={computers}")

    if user==computers:
        print("Both players selected{user}.It's a tie!")
    elif user=="Rock":
        if computers=="Scissors":
            print("Rock smashes scissors!You win!")
        else:
            print("Paper covers rock!You lose.")
    elif user=="Paper":
        if  computers=="Rock":
            print("Paper covers rock!You win!")
        else:
            print("Scissors cuts paper!You lose.")
    elif user=="Scissors":
        if  computers=="Paper":
            print("Scissors cuts paper!You win!")
        else:
            print("Rock smashes scissors!You lose.")

    re_play=input("Replay?(y/n): ")
    if re_play.lower()!= "y":
        break
