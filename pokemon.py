#yahir
#pokemon.py
#trains pokemon
import random

#functions
pokemon_level= 0
pokemon_name= "Charmander"
day= 1

def main():
    print("Welcome to Pokemon")
    global pokemon_level
    global pokemon_name
    global day
    while True:
        decision=input("What will you like to do today: ")
        if decision == "Train":
            pokemon_level= pokemon_level + 1
            day= day + 1
            evolve()
            print_images()
            print(f"{pokemon_name} is now level {pokemon_level}")
            print("day " + str(day))
            forward= input("Would you like to do something else: ")
            if forward== "Yes":
                continue
            elif forward == "No":
                break
            else:
                break
        elif decision == "Battle":
            outcome= random.randint(1,2)
            if outcome == 1:
                pokemon_level= pokemon_level + 2
                day= day + 1
                evolve()
                print_images()
                print("You won!!!")
                print(f"{pokemon_name} has now level {pokemon_level}")
                forward= input("Would you like to do something else: ")
                if forward == "Yes":
                    print("day " + str(day))
                    continue
                elif forward == "No":
                    break
            elif outcome == 2:
                pokemon_level= pokemon_level
                day= day + 1
                evolve()
                print_images()
                print("You lost. Boo")
                print(f"{pokemon_name} is still at level {pokemon_level}")
                forward= input("Would you like to do something else: ")
                if forward == "Yes":
                    print("day " + str(day))
                    continue
                elif forward == "No":
                    break
                else:
                    break
        else:
            print("I don't understand")
            print("Please type Train or Battle")
            continue

def evolve():
    global pokemon_name
    global pokemon_level
    if pokemon_level >= 10:
        pokemon_name= "Charizard"
    elif pokemon_level >= 5:
        pokemon_name= "Charmeleon"

def print_images():
    global pokemon_name
    if pokemon_name== "Charmander":
        charmander()
    elif pokemon_name== "Charmeleon":
        charmeleon()
    elif pokemon_name== "Charizard":
        charizard()

def charmander():
    print((r"             _.--\"\"`-..\n"))
    print((r"           ,'          `.\n"))
    print((r"         ,'          __  `.\n"))
    print((r"        /|          \" __   \\\n"))
    print((r"       , |           / |.   .\n"))
    print((r"       |,'          !_.'|   |\n"))
    print((r"     ,'             '   |   |\n"))
    print((r"    /              |`--'|   |\n"))
    print((r"   |                `---'   |\n"))
    print((r"    .   ,                   |                       ,\".\n"))
    print((r"     ._     '           _'  |                    , ' \\ `\n"))
    print((r" `.. `.`-...___,...---\"\"    |       __,.        ,`\"   L,|\n"))
    print((r" |, `- .`._        _,-,.'   .  __.-'-. /        .   ,    \\\n"))
    print(("-:..     `. `-..--_.,.<       `\"      / `.        `-/ |   .\n"))
    print((r" `,         \"\"\"\"'     `.              ,'         |   |  ',,\n"))
    print((r"   `.      '            '            /          '    |'. |/\n"))
    print((r"     `.   |              \\       _,-'           |       ''\n"))
    print((r"       `._'               \\   '\"\\                .      |\n"))
    print((r"          |                '     \\                `._  ,'\n"))
    print((r"          |                 '     \\                 .'|\n"))
    print((r"          |                 .      \\                | |\n"))
    print((r"          |                 |       L              ,' |\n"))
    print((r"          `                 |       |             /   '\n"))
    print((r"           \\                |       |           ,'   /\n"))
    print((r"         ,' \\               |  _.._ ,-..___,..-'    ,'\n"))
    print((r"        /     .             .      `!             ,j'\n"))
    print((r"       /       `.          /        .           .'/\n"))
    print((r"      .          `.       /         |        _.'.'\n"))
    print((r"       `.          7`'---'          |------\"'_.'\n"))
    print((r"      _,.`,_     _'                ,''-----\"'\n"))
    print((r"  _,-_    '       `.     .'      ,\\\n"))
    print((r"  -\" /`.         _,'     | _  _  _.|\n"))
    print((r"   \"\"--'---\"\"\"\"\"'        `' '! |! /\n"))
    print((r"                           `\" \" -' mh\n"))
    print(("\n"))
    print(("\n"))

def charmeleon():
    print((r"                     ,-'`\\\n"))
    print((r"                 _,\"'    j\n"))
    print((r"          __....+       /               .\n"))
    print((r"      ,-'\"             /               ; `-._.'.\n"))
    print((r"     /                (              ,'       .'\n"))
    print((r"    |            _.    \\             \\   ---._ `-.\n"))
    print((r"    ,|    ,   _.'  Y    \\             `- ,'   \\   `.`.\n"))
    print((r"    l'    \\ ,'._,\\ `.    .              /       ,--. l\n"))
    print((r" .,-        `._  |  |    |              \\       _   l .\n"))
    print((r"/              `\"--'    /              .'       ``. |  )\n"))
    print((".\\    ,                 |                .        \\ `. '\n"))
    print(("`.                .     |                '._  __   ;. \\'\n"))
    print((r" `-..--------...'       \\                  `'  `-\"'.  \\\n"))
    print((r"     `......___          `._                        |  \\\n"))
    print((r"              /`            `..                     |   .\n"))
    print((r"             /|                `-.                  |    L\n"))
    print((r"            / |               \\   `._               .    |\n"))
    print((r"          ,'  |,-\"-.   .       .     `.            /     |\n"))
    print((r"        ,'    |     '   \\      |       `.         /      |\n"))
    print((r"      ,'     /|       \\  .     |         .       /       |\n"))
    print((r"    ,'      / |        \\  .    +          \\    ,'       .'\n"))
    print((r"   .       .  |         \\ |     \\          \\_,'        / j\n"))
    print((r"   |       |  L          `|      .          `        ,' '\n"))
    print((r"   |    _. |   \\          /      |           .     .' ,'\n"))
    print((r"   |   /  `|    \\        .       |  /        |   ,' .'\n"))
    print((r"   |   ,-..\\     -.     ,        | /         |,.' ,'\n"))
    print((r"   `. |___,`    /  `.   /`.       '          |  .'\n"))
    print((r"     '-`-'     j     ` /.\"7-..../|          ,`-'\n"))
    print((r"               |        .'  / _/_|          .\n"))
    print((r"               `,       `\"'/\"'    \\          `.\n"))
    print((r"                 `,       '.       `.         |\n"))
    print((r"            __,.-'         `.        \\'       |\n"))
    print((r"           /_,-'\\          ,'        |        _.\n"))
    print((r"            |___.---.   ,-'        .-':,-\"`\\,' .\n"))
    print((r"                 L,.--\"'           '-' |  ,' `-.\\\n"))
    print((r"                                       `.' mh\n"))

def charizard():
    print((r"                .\"-,.__\n"))
    print((r"                `.     `.  ,\n"))
    print((r"             .--'  .._,'\"-' `.\n"))
    print((r"            .    .'         `'\n"))
    print((r"            `.   /          ,'\n"))
    print((r"              `  '--.   ,-\"'\n"))
    print((r"               `\"`   |  \\\n"))
    print((r"                  -. \\, |\n"))
    print((r"                   `--Y.'      ___.\n"))
    print((r"                        \\     L._, \\\n"))
    print((r"              _.,        `.   <  <\\                _\n"))
    print((r"            ,' '           `, `.   | \\            ( `\n"))
    print((r"         ../, `.            `  |    .\\`.           \\ \\_\n"))
    print((r"        ,' ,..  .           _.,'    ||\\l            )  '\".\n"))
    print((r"       , ,'   \\           ,'.-.`-._,'  |           .  _._`.\n"))
    print((r"     ,' /      \\ \\        `' ' `--/   | \\          / /   ..\\\n"))
    print((r"   .'  /        \\ .         |\\__ - _ ,'` `        / /     `.`.\n"))
    print((r"   |  '          ..         `-...-\"  |  `-'      / /        . `.\n"))
    print((r"   | /           |L__           |    |          / /          `. `.\n"))
    print((r"  , /            .   .          |    |         / /             ` `\n"))
    print((r" / /          ,. ,`._ `-_       |    |  _   ,-' /               ` \\\n"))
    print((r"/ .           \\\"`_/. `-_ \\_,.  ,'    +-' `-'  _,        ..,-.    \\`.\n"))
    print((".  '         .-f    ,'   `    '.       \\__.---'     _   .'   '     \\ \\\n"))
    print(("' /          `.'    l     .' /          \\..      ,_|/   `.  ,'`     L`\n"))
    print(("|'      _.-\"\"` `.    \\ _,'  `            \\ `.___`.'\"`-.  , |   |    | \\\n"))
    print(("||    ,'      `. `.   '       _,...._        `  |    `/ '  |   '     .|\n"))
    print(("||  ,'          `. ;.,.---' ,'       `.   `.. `-'  .-' /_ .'    ;_   ||\n"))
    print(("|| '              V      / /           `   | `   ,'   ,' '.    !  `. ||\n"))
    print(("||/            _,-------7 '              . |  `-'    l         /    `||\n"))
    print((". |          ,' .-   ,' ||               | .-.        `.      .'     ||\n"))
    print((r"`'        ,'    `\".'    |               |    `.        '. -.'       `'\n"))
    print((r"         /      ,'      |               |,'    \\-.._,.'/'\n"))
    print((r"         .     /        .               .       \\    .''\n"))
    print((r"       .`.    |         `.             /         :_,'.'\n"))
    print((r"         \\ `...\\   _     ,'-.        .'         /_.-'\n"))
    print((r"          `-.__ `,  `'   .  _.>----''.  _  __  /\n"))
    print((r"               .'        /\"'          |  \"'   '_\n"))
    print((r"              /_|.-'\\ ,\".             '.'`__'-( \\\n"))
    print((r"                / ,\"'\"\\,'               `/  `-.|\" mh\n"))


#main
main()
