# Define the rooms and their descriptions
rooms = {
    "Corridor": "You are in a corridor links to the main hall and lifts.",
    "Main Hall": "You are in the main hall. There is a grand chandelier hanging from the ceiling, has immense L-shaped coach and a long desk. Looks like people using this area for leisure time.",
    "Manager's Office": "You are in the manager's room. There is a desk with a comfy office chair. Look, that's the key!!",
    "Meeting Room": "You are in the meeting room. There is a long conference table.",
    "Team Leader's Office": "You are in the team leader's office.",
    "Emergency Exit": "You are in the emergency room. The walls are covered in symbols leading to the emergency exit",
    "Big Office": "You are in a big office. It is spacious and well-lit. There are several cubicles",
    "Kitchen": "You are in the kitchen.",
    "Balcony": "You are on the balcony. You have a view of the garden below."
}



# Define the room connections
room_connections = {
    "Main Hall": {"north": "Balcony", "south": "Corridor", "northwest": "Manager's Office", "southwest": "Team Leader's Office", "northeast": "Emergency Exit", "east": "Big Office", "southeast": "Kitchen", "west": "Team Leader's Office"},
    "Corridor": {'north': 'Main Hall'},
    "Manager's Office": {"east": "Main Hall", "north": "Balcony", "south": "Meeting Room"},
    "Team Leader's Office": {"north": "Meeting Room", "east": "Main Hall"},
    "Balcony": {'south': 'Main Hall', 'southwest': 'Manager Room'},
    "Meeting Room": {"north": "Manager Room", "south": "Team Leader's Office", 'west': 'Main Hall'},
    "Emergency Exit": {'east': 'Main Hall'},
    "Big Office": {'west': 'Main Hall', 'south': 'Kitchen'},
    "Kitchen": {'north': 'Big Office', 'east': 'Main Hall'},
}

print("Welcome!! You are the manager of a company and you are left alone in the office because you are working overtime. Just as you were leaving, you realized you forgot your card, so you can't use the lift. You need to go to your room and get your card. Good luck!")
print("You are in the corridor now and you need to reach your key with the options in front of you. Good luck")


# Initialize the player's position
current_room = "Corridor"

# Main game loop
keys_found = False
should_continue = True

while should_continue:
    # Display the current room's description
    print(rooms[current_room])

    # List available directions
    available_directions = room_connections[current_room].keys()
    print('Available directions:', ', '.join(available_directions))

    # Get user input
    user_input = input('Enter your move (e.g., "north", "east", "south", "west", "southwest", "southeast", "northeast", "northwest" or "quit" to get help and finish the game): ').lower()

    # Check if the user wants to quit the game
    if user_input == 'quit':
        print('Ok we are calling the Officer to help you. Thank you for playing')
        should_continue = False
    else:
        # Check if the entered direction is valid
        if user_input in available_directions:
            current_room = room_connections[current_room][user_input]
            if current_room == "Manager's Office":
                keys_found = True
                print("Congratulations! You found the keys. You can now leave the office.")
                should_continue = False
        else:
            print("You can't move in that direction. Try a different direction or 'quit'.")
    
if keys_found:
    print("Thank you for playing. You successfully found the keys and can now leave the office.")
else:
    print("Thank you for playing. Better luck next time!")