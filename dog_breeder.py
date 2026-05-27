#yahir
#dog_breeder.py
#Create a project that meets the requirements of the CREATE task.

#initialize
import webbrowser
import pandas as pd

dogs = pd.read_csv('Yahir Ramos-Baldoky - dogs - Sheet1.csv')
weight_min = dogs['Minimum Weight'].tolist()                                  #]
name = dogs['Name'].tolist()                                                  #]
reason = dogs['BredFor'].tolist()                                             #] Goal 1
image = dogs['Image'].tolist()                                                #]
description = dogs['Temperament'].tolist()                                    #]
filtered_list = []


#function
def getDogSize(size):                                                         #] Goal 2
    for i in range(len(weight_min)):
        if size == "tiny":
            if weight_min[i] < 10 or weight_min[i] == 10:
                filtered_list.append(name[i])
        elif size == "small":
            if weight_min[i] > 10 and weight_min[i] < 25 or weight_min[i] == 25:
                filtered_list.append(name[i])
        elif size == "medium":
            if weight_min[i] > 25 and weight_min[i] < 60 or weight_min[i] == 60:
                filtered_list.append(name[i])
        elif size == "large":
            if weight_min[i] > 60:
                filtered_list.append(name[i])
    print(filtered_list)
    filtered_list.clear()

def breedOfDog(breed_name):                                                   #] Goal 3
    for i in range(len(name)):
        if breed_name == name[i]:
            webbrowser.open(image[i])
            print(description[i])

def purposeOfDog(purpose):                                                    #] Goal 4
    for i in range(len(reason)):
        if purpose in reason[i]:
            filtered_list.append(name[i])
    print(filtered_list)
    filtered_list.clear()

def dogChooser():                                                             #] Goal 5
    print("Welcome to Dog Chooser!!")
    while True:
        filtered = input("""How will you like to find a dog?
Base on size? purpose? or breed? """)
        if filtered == "size":
            size = input("""What size will you like your dog to be?
tiny, small, medium, or large? """)
            getDogSize(size)
            continue_end = input("Are satisfied with your options? ")
            if continue_end == "yes":
                print("Thank you for choosing our service. Have a nice day")
                break
        elif filtered == "purpose":
            purpose = input("Why do you want a dog? ")
            purposeOfDog(purpose)
            continue_end = input("Are satisfied with your options? ")
            if continue_end == "yes":
                print("Thank you for choosing our service. Have a nice day")
                break
        elif filtered == "breed":
            breed_name = input("What breed are you looking for? ")
            breedOfDog(breed_name)
            continue_end = input("Are satisfied with your options? ")
            if continue_end == "yes":
                print("Thank you for choosing our service. Have a nice day")
                break


#main

getDogSize("small")

breedOfDog("Pug")

purposeOfDog("Lapdog")

dogChooser()


#Sources Of Information

#Dog Dataset
#Website Name: Code.org
#URL: https://code.org/en-US
#Dataset Source:https://thedogapi.com/en

