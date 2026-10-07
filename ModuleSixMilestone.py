##Gervasi, Brandon

#A dictionary for the simplified dragon text game
#The dictionary links a room to other rooms.
rooms = {
        'Great Hall': {'South': 'Bedroom'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
        'Cellar': {'West': 'Bedroom'}
    }


#start the player in the great hall
current_room = 'Great Hall'

#start main loop
while current_room != 'exit':

    #display the current room
    print(f'You are in the {current_room} room.')

    #list exits
    exits = rooms[current_room]
    print(f'Available exits: {', '.join(exits.keys())}')

    #player input
    command = input('Please enter command: ')

    #exit statement
    if command.lower() == 'exit':
        current_room = 'exit'

    #movement commands
    elif command.lower().startswith('go '):
        direction = command[3:].capitalize()

        if direction in exits:
            current_room = exits[direction]
        #invalid direction
        else:
            print(f'This path is blocked')
    #invalid commands
    else:
        print(f'Invalid command please try again')
#end loop or exit command input
print('Thanks for playing!')