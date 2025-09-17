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
   
    if directions == "quit":
        print("Thanks for playing!")
        break
    
    if directions != "north" and directions != "south" and directions != "east" and directions != "west":
        print("Invalid direction. Please enter north, south, east, west, or quit.")
        continue




inventory = []  
for item in rooms:
    if item == "item":
        inventory.append(rooms[Current_Room][item])
        print(f"You have found a {rooms[Current_Room][item]}!")