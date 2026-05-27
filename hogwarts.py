#yahir
#hogwarts.py
#Create a program that prompts the user for their name and simulates being assigned one of the 4 hogwarts houses

#Initialize
import time
import random

#function
def main():
    print("Welcome to Hogwarts")
    name=input("What is your name: ")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print ("....")
    time.sleep(1)
    print("......")
    print( house(name) )

def house(name):
    if name == "Harry" or name == "Ron" or name == "Hermione":
        return "Gryffindor"
    elif name == "Newt" or name == "Nymphadora" or name == "Pomona":
        return "Hufflepuff"
    elif name == "Lune" or name == "Cho" or name == "Filius":
        return "Ravenclaw"
    elif name == "Voldemort" or name == "Draco" or name == "Severus":
        return "Slytherin"
    else:
        num = random.randint(1,4)
        if num == 1:
            return "Gryffindor"
        elif num == 2:
            return "Hufflepuff"
        elif num == 3:
            return "Ravenclaw"
        elif num == 4:
            return "Slytherin"


#main
main()







