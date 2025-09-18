rooms = {
    "start": {"north":"Hall", "south":"Kitchen", "east":"Dining Room", "west":"Garden"},
    "Hall": {"south": "Kitchen", "east": "Dining Room", "west": "Garden","item": "key"},
            "Kitchen": {"north": "Hall", "west": "Garden", "east": "Dining Room", "item": "potion"},
            "Dining Room": {"north": "Hall", "west": "Garden", "south": "Kitchen", "item": "dagger"},
            "Garden": {"east": "Dining Room", "north": "Hall", "south": "Kitchen", "item": "shield"}}

Current_Room = "start"
while True:
    print(f"You are in the {Current_Room}.")
    directions = str(input("Enter a direction (north, south, east, west, or quit): ")).lower()
   
    if "item" in rooms[Current_Room]:
        item_found = rooms[Current_Room]["item"]
        print(f"You see a {rooms[Current_Room]["item"]} here.")
        
        if item_found == "key":
            print("You have found the key! You win!")
            break
        if item_found == "dagger":
            print("You have found the dagger! You Lose!")
            break
        else:
            print ("You have found an item, but it doesn't help you win or lose.")
            continue
            

    if directions == "quit":
        print("Thanks for playing!")
        break
    
    elif directions in rooms[Current_Room]:
        Current_Room = rooms[Current_Room][directions]
    else:
        print("You can't go that way.")

