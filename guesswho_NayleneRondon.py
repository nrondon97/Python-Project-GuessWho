#------------------------------------------------------------------------------------------------------------------------
# Program name – guesswho_NayleneRondon.py
# Written by – Naylene Rondon
# Date – 4/3/2017
# It's a murder mystery style guess game using dictionaries.
#--------------------------------------------------------------------------------------------------------------------------
import random
import time

def main():
    """Main Function"""
    townsmembers = ["Maria", "Charlotte", "Daniel", "Peter", "Bonnie", "Anthony", "Sarah", "Joshua"]
    intro(townsmembers)
    replay = "yes"

    while replay != "no":
        #Variables
        townsmembers = ["Maria", "Charlotte", "Daniel", "Peter", "Bonnie", "Anthony", "Sarah", "Joshua"]
        townroles = charactersRandom(townsmembers)
        dead = []
        town = Dict(townsmembers,townroles)
        #print(town) #Test
        night(town)
        replay = input("Do you want to play again? ")

def intro(town):
    """Introduction"""
    print("Along the edge of the sea is a small town.")
    time.sleep(2)
    print("The people are quiet and the town is crimefree. Or is it?")
    time.sleep(2)
    print("Rumors had spread one of the neighbors is a member of the mafia.")
    time.sleep(2)
    print("The mafia has a hit list tonight.")
    time.sleep(2)
    print("But they know the town laws.")
    time.sleep(2)
    print("If they're caught they'll be killed.")
    time.sleep(2)
    print("To save his own skin...")
    time.sleep(2)
    print("They'll have to survive every night until")
    time.sleep(2)
    print("They can kill everyone in town.")
    time.sleep(2)
    print("Can you find the mafia?")

    print("These are the town members:")
    for key in town:
        print(key)


def charactersRandom(townsroles):
    """Define roles in random"""
    townroles = ["townsperson", "townsperson", "townsperson", "townsperson", "townsperson", "townsperson", "townsperson", "townsperson"]
    mafia = 0
    doctor = 0
    while doctor == mafia:
        mafia = random.randint(0,len(townsroles)-1)  #Places mafia in random location
        doctor = random.randint(0,len(townsroles)-1)  #places doctor in random location

    townroles[mafia] = "mafia"
    townroles[doctor] = "doctor"

    #print(townroles)  #Test

    return townroles
    
def Dict(townsmembers,townroles):
    """Makes dicitionary entries"""
    town = {
            townsmembers[0] : townroles[0],
            townsmembers[1] : townroles[1],
            townsmembers[2] : townroles[2],
            townsmembers[3] : townroles[3],
            townsmembers[4] : townroles[4],
            townsmembers[5] : townroles[5],
            townsmembers[6] : townroles[6],
            townsmembers[7] : townroles[7]
            }


    return town

def dead(town):
    """Randomly kills someone"""
    #print(town)  #Test
    ranDeath = random.choice(list(town.keys()))

    #print(ranDeath) #Test

    while town[ranDeath] == "mafia":
        ranDeath = random.choice(list(town.keys()))

    return ranDeath

def choice(town, dead_person):
    """Allows user to input"""
    user_choice = input("Who do you think killed " + dead_person + "? ")
    #Prevents user from an invalid choice such as a memeber already dead.
    if user_choice == dead_person:
        print("They didn't kill themselves.")
        user_choice = input("Who do you think killed " + dead_person + "? ")
        
    while user_choice not in town.keys():
        print("Please chose a living townsmember.")
        user_choice = input("Who do you think killed " + dead_person + "? ")

    return user_choice

def valid(town, user_choice):
    """Compares input with mafia"""
    for key, value in town.items(): 
        if user_choice == key:  #Win
            if value == "mafia":
                print("You found the mafia! You won!")
                town = {key:value}
                break
                

            else:  #Fail
                print("They weren't the mafia. You killed an innocent person.")

                del town[key]
                break

    return town

def townalibi(town, dead):
    alibi = ["Poor " + dead + ". They were like family to me." , "It's sad, but I didn't know them too well.", "I haven't seen " + dead + " all day.", "Never knew them too well. I like to keep to myself.", "Shame, " + dead + " was a nice person.", "How sad!", "Oh no!" ]

    for member in town.keys():
        print(member + " alibi:")
        print(random.choice(alibi)+"\n")

def night(town):
    """Replays each night of death"""
    survivors = len(town)

    while survivors > 2: #Loop until mafia is found or players fails
        print("The sun slowly setting beyond the horizon.")
        time.sleep(2)
        print("It is now nighttime.")

        Death = dead(town)

        del town[Death]

        print(Death + " has died.")
        townalibi(town, Death)

        user = choice(town, Death)

        town = valid(town, user)

        survivors = len(list(town.keys()))


    
#Calls main function
main()
