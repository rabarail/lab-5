"""Program name: Dice rolling
AUthor: Rajani Baraili
Purpose: rolls two dice and prints outcome  based on table
Starter code: None
Date:02/09/2026"""
import random
print("Welcome to the dice rolling game!")
die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
total= die1 + die2
if (die1==1 and die2==1):
    print("Snake Eyes")
elif (die1==1 and die2==2) or (die1==2 and die2==1):
    print("Ace Caught a Deuce")
elif (die1==2 and die2==2):
    print("Little Joe from Kokomo")
elif (die1==1 and die2==4) or (die1==4 and die2==1):
    print("Little Phoebe")
elif (die1==2 and die2==3) or (die1==3 and die2==2):
    print("Little Phoebe")
elif (die1==3 and die2==3):
    print("Jimmy Hicks from the Sticks")
elif (die1==1 and die2==6) or (die1==6 and die2==1):
    print("Six Ace")
elif (die1==4 and die2==4):
    print("Eighter from Decatur")
elif (die1==3 and die2==6) or (die1==6 and die2==3):
    print("Nina from Pasadena")
elif (die1==4 and die2==5) or (die1==5 and die2==4):
    print("Nina from Pasadena")
elif (die1==5 and die2==5):
    print("Puppy Paws")
elif (die1==6 and die2==5) or (die1==5 and die2==6):
    print("Six Five no Jive")
elif (die1==6 and die2==6):
    print("Boxcars")
print("The total is", total)