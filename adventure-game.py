
# Creating the Game Structure
"""
Our game will have a simple structure with rooms and actions. 
The player will navigate the rooms and interact with the environment by typing commands. 
Let's start by defining the rooms and their descriptions.
"""
rooms = {
    'start': {
        'description': '\nYou are in the reception room.',
        'north': 'dining room'
    },
    'dining room': {
        'description': '\nYou are in the dining room.',
        'east': 'kitchen',
        'south': 'start'
    },
    'kitchen': {
        'description': '\nYou are in the kitchen.',
        'west': 'dining room',
        'south': 'bedroom'
    },
    'bedroom': {
        'description': '\nYou are in the bedroom. You found the treasure! Congratulations!',
        'end': True
    }
}

# Creating a function to display the room description and available actions
def show_room(room):
    print(room['description'])

    if 'north' in room:
        print('There is a door to your north.')
    if 'east' in room:
        print('There is a door to your east.')
    if 'south' in room:
        print('There is a door to your south.')
    if 'west' in room:
        print('There is a door to your west.')

# Handling User Input
# Creating a function to handle user input and process the commands
def get_action(room):
    while True:
        action = input('Where do you want to go? ').lower().strip()

        if action == 'north' and 'north' in room:
            return room['north']
        elif action == 'east' and 'east' in room:
            return room['east']
        elif action == 'south' and 'south' in room:
            return room['south']
        elif action == 'west' and 'west' in room:
            return room['west']
        else:
            print('Invalid action. Try again.')

# Main Game Loop
# Creating the main game loop that will keep running until the player reaches the end
current_room = rooms['start']

while 'end' not in current_room:
    show_room(current_room)
    next_room = get_action(current_room)
    current_room = rooms[next_room]

print(current_room['description'])