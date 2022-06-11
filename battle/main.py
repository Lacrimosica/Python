from classes.game import Person, bcolors

magic = [{"name": "Fire", "cost": 10, "dmg" : 10},
         {"name": "Thunder", "cost": 10, "dmg" : 10},
         {"name": "Blizzard", "cost": 10, "dmg" : 10}]

Player = Person(460, 65, 60, 34, magic)

enemy = Person(1200, 65,45,25, magic)


running = True

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS" , bcolors.ENDC)

while running: 
    print("==============================")
    Player.choose_action()
    choice = input("choose action: ")
    index = choice - 1

    print("your choice" , index)
    running = False
