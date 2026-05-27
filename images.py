#yahir
#images.py
#Create a Python program that displays an image and a description from a selected theme each time the user desires a recommendation. The images must be stored as URLs in an array. Additionally, you will have an array of descriptions to go along with the images.

#Initialize
import webbrowser

#Function
def dog_recommender():
    print("Welcome to Dog Recommender!!")
    purpose = input("Why do you want a dog? For guard or friend? ")
    if purpose == "guard":
        size = input("Would size would you want your dog to be? Big or small? ")
        if size == "big":
            webbrowser.open(url[0])
            print(descriptions[0])
        elif size == "small":
            webbrowser.open(url[1])
            print(descriptions[1])
        else:
            print("I don't understand. Goodbye")
    elif purpose == "friend":
        size = input("Would size would you want your dog to be? Big or small? ")
        if size == "big":
            webbrowser.open(url[2])
            print(descriptions[2])
        elif size == "small":
            webbrowser.open(url[3])
            print(descriptions[3])
        else:
            print("I don't understand. Goodbye")


url = [ "https://cdn.britannica.com/79/232779-050-6B0411D7/German-Shepherd-dog-Alsatian.jpg",            #German Shepherd
       "https://www.carecredit.com/sites/cc/image/hero_dachshund_dog_breed.jpg",                         #Dachshund
       "https://imageserver.petsbest.com/marketing/news/Austrailian%20Cattle.jpg",                       #Blue Heeler
       "https://c.files.bbci.co.uk/17444/production/_124800359_gettyimages-817514614.jpg"                #Pug
       ]

descriptions = ["German Shepherds are widely know to be guard dogs. They are highly intelligent. They are even used by the police",
                "While they may be small, Dachshunds are highly protective and loyal to their owners. This makes them perfect for a small guard dog",
                "Blue Heelers are adorable dogs and super energetic. They are very loyal and protect their owners but not to the extreme like guard dogs",
                "Pugs are super cute dogs that can help with anxiety and depression. They are perfect friends for kids and teenagers"]

#Main
dog_recommender()


#Sources of Information

#German Shepherd standing on grass
#Website Name:Britannica
#URL: https://www.britannica.com/animal/German-shepherd
#Author Name: Caroline Coile
#Date: Feb 7, 2026
#Article Title: German Shepherd

#Dachshund staring at camera smiling
#Website Name: CareCredit
#URL: https://www.carecredit.com/well-u/pet-care/dachshund-dog-breed/
#Author Name: Jean Marie Bauhaus
#Date: January 24, 2025
#Article Title: Dachshund Dog Breed Guide

#Blue Heeler smiling
#Website Name: PetsBest
#URL: https://www.petsbest.com/blog/australian-cattle-dog
#Author Name: Dr. Jack L. Stephens
#Date: Aug 2, 2011
#Article Title: Australian Cattle Dog – Blue Heeler

#Pug staring at camera
#Website Name: BBC
#URL: https://www.bbc.com/news/newsbeat-61494094
#Author Name: Manish Pandey
#Date: 18 May 2022
#Article Title: Pug health so poor it 'can't be considered a typical dog' - study





