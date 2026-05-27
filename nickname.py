#yahir
#nickname.py
#Asks for preferences and recommends a superperson character

print("Welcome to Superperson Guesser")

#function
def superperson():
    team = input("Do you want prefer the Avengers or the Justice League?: ")     #collect 1st input from user
    if team == "Avengers":
        movie = input("Which was your favorite movie, Thor Movie or Iron Man 1?: ")
        if movie == "Thor Movie":
            moral = input("Did you root for the Bad Guy or Good Guy?: ")
            if moral == "Bad Guy":
                print("Loki")
            elif moral == "Good Guy":
                print("Thor")
        elif movie == "Iron Man 1":
            moral = input("Did you root for the Bad Guy or Good Guy?: ")
            if moral == "Bad Guy":
                print("Ultron")
            elif moral == "Good Guy":
                print("Iron Man")
    elif team == "Justice League":
        movie = input("Which was your favorite movie, The Flash or Dark Knight?: ")
        if movie == "The Flash":
            moral = input("Did you root for the Bad Guy or Good Guy?: ")
            if moral == "Bad Guy":
                print("Reverse-flash")
            elif moral == "Good Guy":
                print("The Flash")
        elif movie == "Dark Knight":
            moral = input("Did you root for the Bad Guy or Good Guy?: ")
            if moral == "Bad Guy":
                print("Joker")
            elif moral == "Good Guy":
                print("Batman")


#main
superperson()
