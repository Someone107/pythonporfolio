#albums.py
#help users find their new favorite albums

#initialize
import pandas
import time #Using time made the program more user friendly

rolling_stone = pandas.read_csv('Rolling Stone_ 500 Albums - Sheet1.csv')
genre = rolling_stone['Genre'].tolist()
subgenre = rolling_stone['Subgenre'].tolist() #simple names for the list makes the code easier to understand
year = rolling_stone['Year'].tolist()
albums = rolling_stone['Album'].tolist()
bands = rolling_stone['Artist'].tolist()
all_genre = ["Rock", "Pop", "Funk/Soul", "Blues", "Jazz", "Folk",
             "World", "Country", "Classical", "Stage & Screen",
             "Reggae", "Hip Hop", "Electronic", "Latin"] #providing the user a list for reference made it easier to type input
filtered_list_1 = [] #having multiple filter list make the code more organized
filtered_list_2 = []
filtered_list_3 = []
filtered_list_4 = []

print("Welcome to Album Finder!!")

#function

def find_genre(favorite_genre):
    for i in range (len(genre)):
        if favorite_genre in genre[i]:
            filtered_list_1.append(albums[i])
    print(filtered_list_1)
    if (len(filtered_list_1)) == 0:
        print('Sorry. There arent any matches for you :(') #providing a line of code to inform the user instead of just having a error makes the code more ser friendly

def find_band(favorite_band):
    for i in range (len(bands)):
        if favorite_band in bands[i]:
            filtered_list_2.append(albums[i])
    print(filtered_list_2)
    if (len(filtered_list_2)) == 0:
        print('Sorry. There arent any matches for you :(')

def find_year():
    favorite_year_1 = input('What is the year of the newest song you like? ')
    favorite_year_2 = input('What is the year of the oldest song you like? ')
    for i in range (len(year)):
        if int(favorite_year_1) >= year[i] and year[i] >= int(favorite_year_2): #the usage of and makes the code more simplistic and less longer
            filtered_list_3.append(albums[i])
    time.sleep(2)
    print('...')
    time.sleep(2)
    print(filtered_list_3)
    if (len(filtered_list_3)) == 0:
        print('Sorry. There arent any matches for you :(')

def perfect_albums():
    matches = set(filtered_list_1).intersection(filtered_list_2,filtered_list_3) #using .intersection() made the code more efficient in searching through the dataset
    if (len(matches)) == 0:
        print('Sorry. There isnt a perfect album for you :(')
    elif (len(matches)) > 0:
        print(matches)
        print('These are your perfect albums!! YAY') #the conversational tone makes the program more fun

def fav_album():
    while True:
        decision = input('''How will you like to find your next favorite albums?
genre? band? or year? all? ''').lower()
        if decision == 'genre':
            print('This will search for albums that match your favorite genre')
            print('Choose from one of the genres listed below ')
            print(all_genre)
            favorite_genre = input('What is your favorite genre? ')
            capitalized_fav = favorite_genre.capitalize() #Using .capitalize() makes the code more user friendly and prevents crashing
            time.sleep(2)
            print('...')
            time.sleep(2)
            find_genre(capitalized_fav)
            continue_end = input("Are satisfied with your options? ").lower()
            if continue_end == "yes":
                print("Thank you for choosing our service(◠‿◠) Have a nice day!!") #Using emojis kept the program engaging!
                break
            elif continue_end == 'no':
                continue
            else:
                print('I dont understand. Come back again')
                print("Thank you for choosing our service(◠‿◠) Have a nice day!!")
                break
        elif decision == 'band':
            print('This will search for albums that are from your favorite band')
            favorite_band = input('Who is your favorite band? ')
            capitalized_fav = favorite_band.title()
            time.sleep(2)
            print('...')
            time.sleep(2)
            find_band(capitalized_fav)
            continue_end = input("Are satisfied with your options? ").lower()
            if continue_end == "yes":
                print("Thank you for choosing our service(◠‿◠) Have a nice day!!")
                break
            elif continue_end == 'no':
                continue
            else:
                print('I dont understand. Come back again')
                print("Thank you for choosing our service(◠‿◠) Have a nice day!!")
                break
        elif decision == 'year':
            print('This will search for albums released on your favorite music era')
            print('Answers must be between 1955 to 2011') #gives the user a range of options to prevent a error
            find_year()
            continue_end = input("Are satisfied with your options? ").lower()
            if continue_end == "yes":
                print("Thank you for choosing our service(◠‿◠) Have a nice day!!")
                break
            elif continue_end == 'no':
                continue
            else:
                print('I dont understand. Come back again')
                print("Thank you for choosing our service(◠‿◠) Have a nice day!!")
                break
        elif decision == 'all':
            print('This compares all 3 lists and finds the common albums between them. The PERFECT albums for YOU!!!')
            ultimate_option = input('This can only be used if all 3 ways were used. Did you use all 3? ').lower()
            if ultimate_option == 'yes': #these lines of code are great when trying to cover up any error the program may run into
                time.sleep(2)
                print('...')
                perfect_albums()
                print("Thank you for choosing our service(◠‿◠) Have a nice day!!")
                break
            elif ultimate_option == 'no':
                print('Restart the service and take all 3 ways before coming back here')
                print("Thank you for choosing our service(◠‿◠) Have a nice day!!")
                break
            else:
                print('I dont understand. Come back again')
                print("Thank you for choosing our service(◠‿◠) Have a nice day!!")
                break
        else:
            print('I dont understand. Come back again')
            print("Thank you for choosing our service(◠‿◠) Have a nice day!!")
            break

#main
fav_album()

#Sources Of Information

#500 Greatest Albums of All Time as rated by Rolling Stone Magazine
#Website Name: Rolling Stone: 500 Albums
#URL: https://docs.google.com/spreadsheets
#Dataset Source: https://www.kaggle.com/datasets/notgibs/500-greatest-albums

#New code at line 46
#video explaining the importance of Set Intersection
#Website Name: Youtube
#URL: https://www.youtube.com/watch?v=8qohGN4oSMc
#Author Name: TryCoding
#Date: 2021
#Video Title: Set Intersection() Method in Python || Part-47 || Python Tutorial For Beginners
