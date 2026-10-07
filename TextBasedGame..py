# Gervasi, Brandon

# Legend of Zelda Text Adventure

# Room Dictionary defines each room and the items contained within excluding the Start Room
# Only one item will be taken from each room, the unselected item will be lost
# Boos Room excludes items as well

rooms = {
    'Start Room': {
        'North': 'North Room',
        'South': 'South Room',
        'East': 'East Room',
        'West': 'West Room',
    },
    'North Room': {
        'North': 'Boss Room',
        'South': 'Start Room',
        'East': 'Northeast Room',
        'West': 'Northwest Room',
        'item1': 'Shield',
        'item2': 'Backstory scroll'
    },
    'South Room': {
        'North': 'Start Room',
        'item1': 'Health Potion',
        'item2': 'Fire Potion'
    },
    'East Room': {
        'North': 'Northeast Room',
        'West': 'Start Room',
        'item1': 'Whetstone',
        'item2': 'Frost Potion'
    },
    'West Room': {
        'North': 'Northwest Room',
        'East': 'Start Room',
        'item1': 'Damage Resist Potion',
        'item2': 'Health Potion'
    },
    'Northwest Room': {
        'South': 'West Room',
        'East': 'North Room',
        'item1': 'Fire Potion',
        'item2': 'Weakness Scroll'
    },
    'Northeast Room': {
        'South': 'East Room',
        'West': 'North Room',
        'item1': 'Shield Wax',
        'item2': 'Damage Resist Potion'
    },
    'Boss Room': {
        'South' : 'North Room',
    }
}


# Display game functions and instructions


def show_instructions():
    print('=')
    print('        THE LEGEND OF ZELDA: CURSE OF SHADOW GANNON')
    print('=')
    print()
    print('    Long ago after Hyrule was saved by the Hero Link,\nThe Master Sword was returned to the Temple of Time')
    print('    A fragment from Ganondorf broke away before he was destroyed,\na creature you would later know to be called SHADOW GANON')
    print('    Without his body, Ganon has been confined to the deepest dwellings of Hyrule Castle')
    print('    Unable to to fully restore himself, Ganon feeds on darkness and fear to grow stronger\nStrong enough to destroy Hyrule once again')
    print('    In desperation, Ganon has taken Princess Zelda prisoner to drain her of her magic\nto try and rebuild his body')
    print('    You must rescue Zelda before Ganon can return himself to full strength')
    print()
    print('    In order to defeat this Shadow Ganon you must traverse\nHyrule Castle and collect 6 items to grow stronger')
    print('    If you cannot collect 6 items or defeat Ganon,\nall of Hyrule will be lost and the world along with it')
    print()
    print('    Commands')
    print('    --------')
    print('    To Move    : go North, go South, go East, go West\nTo get an item    : get[item name]\nTo use an item    : use[item name]\nTo quit the game    : quit')
    print('=')


#Display current progress


def show_status(current_room, inventory, items_collected, sealed_rooms):
    print('-' * 60)
    print(f'    Room    : {current_room}')
    print(f'    Inventory: {inventory}')
    print(f'    Items  Collected: {items_collected} / 6')
    print(f'    Sealed Rooms: {sealed_rooms}')
    print('-' * 60)


#Show items in current room


    if current_room in sealed_rooms:
        print('Nothing remains, This room has been sealed')

    elif current_room == 'Start Room':
        print('You are in the Temple of Time, Your journey begins here')

    elif current_room == 'Boss Room':
        print('You see though the darkness an imprisoned Zelda and Shadowy Figure')

    else:
        item1 = rooms[current_room].get('item1')
        item2 = rooms[current_room].get('item2')
        if item1 and item2:
            print(f' You see {item1} and {item2} You may choose only one')


#Lore Scrolls


def read_backstory_scroll():
    print('`' * 65)
    print('You unravel the scroll and read:')
    print('Shadow Ganon is not the true Ganondorf. He is but a fragment')
    print('When the Hero of Time struck Ganondorf down, a shred of essence was cast aside.')
    print('Overtime this essence took form, feeding on fear and shadow. He cannot restore')
    print('himself without a proper vessel graced by the Tri-Force. He needs Zelda and he')
    print('needs you. You must not fail.')


def read_weakness_scroll():
    print('`' * 65)
    print('You unravel the scroll and read:')
    print('Shadow Ganon is built from living darkness and as such,')
    print('fire is its natural enemy. Sacred flame disrupts the')
    print('shadow that binds his form, causing it to untether from')
    print('this realm. A fire potion thrown in battle will burn')
    print('his shadow form and deal damage for each turn its lit.')
    print('Pair it with the frost potion to freeze him in place,')
    print('then strike him down with the Master Sword.')


# For items used outside of battle


def use_item(item_name, inventory, sword_damage, damage_resist, player_hearts):

    item_lower = [i.lower() for i in inventory]
    if item_name.lower() not in item_lower:
        print(f'The {item_name} item is not in the inventory')
        return sword_damage, damage_resist, player_hearts

    matched_item = inventory[item_lower.index(item_name.lower())]

    if matched_item == 'Health Potion':
        player_hearts += 3
        inventory.remove(matched_item)
        print(f'\n You drink the health potion. You gain 3 hearts. Hearts: {player_hearts}')

    elif matched_item == 'Damage Resist Potion':
        damage_resist += 2
        inventory.remove(matched_item)
        print('\n You drink the damage resist potion.')
        print(f'Damage resistance increased by 2. Total: {damage_resist}')

    elif matched_item == 'Whetstone':
        sword_damage += 1
        inventory.remove(matched_item)
        print('You sharpen the Master Sword on the Whetstone.')
        print(f'Sword damage increased to {sword_damage}')

    elif matched_item == 'Shield Wax':
        damage_resist += 1
        inventory.remove(matched_item)
        print('You apply the wax to the shield')
        print(f'Damage resistance increased by 1. Total: {damage_resist}')

    elif matched_item == 'Backstory Scroll':
        read_backstory_scroll()

    elif matched_item == 'Weakness Scroll':
        read_weakness_scroll()

    elif matched_item in ('Fire Potion', 'Frost Potion'):
        print('These items may not be used outside of the boss room')

    elif matched_item in ('Master Sword', 'Shield'):
        print('These items are equipped automatically')

    else:
        print('You cannot use {matched_item} currently')

    return sword_damage, damage_resist, player_hearts


# Boss Battle...


def boss_battle(inventory, sword_damage, damage_resist, player_hearts):
    print()
    print('=')
    print('As you slowly enter the room, the darkness stirs')
    print('You see in the center of the room an unconscious')
    print('Zelda. Bound in chains of shadow and pain')
    print('Next to her, Shadow Ganon begins to materialize')
    print('Shadow Ganon: "You will know pain and darkness\nas I have"')
    print('=')

# Boss Stats
    ganon_health = 20
    ganon_max_health = 20
    ganon_base_attack = 3
    ganon_frozen_turns = 0

#Tracking Fire Damage

    fire_turns_remaining = 0
    fire_bonus_damage = 2

# Check for (battle) items brought into boss room

    has_fire_potion = 'Fire Potion' in inventory
    has_frost_potion = 'Frost Potion' in inventory
    has_health_potion = 'Health Potion' in inventory
    shield_equipped = 'Shield' in inventory

#Boss Battle Loop
    while True:
        print(f'Player Health: {player_hearts}')
        print(f'Ganon Health: {ganon_health}/{ganon_max_health}')
        print()
        print('Actions:')
        print('Attack')
        if has_health_potion:
            print('use health potion')
        if has_fire_potion:
            print('use fire potion')
        if has_frost_potion:
            print('use frost potion')

        action = input('Your choice: ').strip().lower()

#Player Actions


        if action == 'attack':
            print(f'You strike Shadow Ganon with the Master Sword! -{sword_damage} health')
            ganon_health -= sword_damage

        elif action == 'use health potion' and has_health_potion:
            player_hearts += 3
            has_health_potion = False
            inventory.remove('Health Potion')
            print('You drink the health potion.\nYour health has been restored by 3 points: {player_hearts}')

        elif action == 'use fire potion' and has_fire_potion:
            fire_turns_remaining = 3
            has_fire_potion = False
            inventory.remove('Fire Potion')
            print('You hurl the Fire Potion at Shadow Ganon\nSacred flame rips through his shadowy form\nhe roars in pain')

        elif action == 'use frost potion' and has_frost_potion:
            ganon_frozen_turns = 2
            has_frost_potion = False
            inventory.remove('Frost Potion')
            print('The bottle smashes open at his feet\nIce has encased his shadowy form\n Ganon is unable to move')

        else:
            print('You cannot use {action} currently')


        # Applying Fire Damage


        if fire_turns_remaining > 0:
            print(f'Sacred flame burns Ganon for {fire_bonus_damage} damage')
            ganon_health -= fire_bonus_damage
            fire_turns_remaining -= 1
            if fire_turns_remaining == 0:
                print('The sacred flames extinguish')

# Check if win conditions have been met

        if ganon_health <= 0:
            print('Shadow Ganon shrieks as the sacred flames consume his form.')
            print('He dissolves into nothing, not dead, but banished from the castle')
            print('You hear a call from the void: "This... is. not. Over."')
            print()
            print('The shadowy chains holding the princess begin to fade as she wakes up')
            print('Zelda: "I knew you would come."')
            return True

# Ganon's turn

        if ganon_frozen_turns > 0:
            print('The shadows lash out from within the ice but cannot move.')
            print(f'({ganon_frozen_turns} frozen turn(s) remaining')
            ganon_frozen_turns -= 1
        else:
            shield_reduction = 2 if shield_equipped else 0
            actual_damage = max(1, ganon_base_attack - shield_reduction - damage_resist)
            player_hearts -= actual_damage
            print(f'Shadow Ganon lashes at you with tendrils wrought in fear\nYou take {actual_damage} damage')

#Check if loss conditions have been met

        if player_hearts <= 0:
            print('Your strength fades as the darkness encroaches.')
            print('Shadow Ganon looms over your body ready to make it his own')
            print('"Finally. A vessel strong enough to contain my power')
            return False


# Main Function


def main():

    current_room = 'Start Room'
    inventory = ['Master Sword']
    sealed_rooms = []
    items_collected = 0
    sword_damage = 2
    damage_resist = 0
    player_hearts = 10

    show_instructions()

    player_name = input('Enter your name: ').strip()
    if not player_name:
        player_name = 'Link'

    print(f'Welcome {player_name}!')
    print('You wake up and find yourself in the temple if time\nA note from Zelda lies at your feet.')
    print('The Master Sword is already in your hands though you are uncertain as to how.')


# Main Game Loop

    while True:
        show_status(current_room, inventory, items_collected, sealed_rooms)
        print()
        command = input('Your Move: ').strip().lower()

        if command == 'quit':
            print('Zelda remains imprisoned. Hyrule will fall to darkness')
            print('Thanks for playing!')
            break

        elif command.startswith('go '):
            direction = command[3:].strip().title()

            if direction in rooms[current_room]:
                target_room = rooms[current_room][direction]

                if target_room == 'Boss Room' and items_collected < 6:
                    print('This door is sealed, You are not strong enough to enter')
                    print(f'Items collected: {items_collected} / 6 required')

                elif target_room in sealed_rooms:
                    print(f'The path to {target_room} is has been sealed.\nTread a different path.')

                else:
                    current_room = target_room
                    print(f'You move {direction.lower()} into the {current_room}')

                    if current_room == 'Boss Room':
                        player_won = boss_battle(inventory, sword_damage, damage_resist, player_hearts)
                        print()

                        if player_won:
                            print('Congratulations, you have saved Hyrule once again\nThanks for playing!')

                        else:
                            print('YOU DIED')
                            print('Thanks for playing, I hope you try again.')

                        break

            else:
                print(f'You cannot go {direction.lower()} from here.')


# Collecting items


        elif command.startswith('get '):
            item_name = command[4:].strip().title()

            if current_room in sealed_rooms:
                print('This room is sealed, there is nothing left here.')

            elif current_room == 'Start Room':
                print('There is nothing to collect here.\nYou may begin your exploration.')

            elif current_room == 'Boss Room':
                print('There is nothing to collect here, only that which lies beyond.')

            else:
                item1 = rooms[current_room].get('item1', '')
                item2 = rooms[current_room].get('item2', '')
                available = [i for i in (item1, item2) if i]

                if item_name in available:
                    inventory.append(item_name)
                    items_collected += 1
                    print(f'You take {item_name} and store it in your pouch.')
                    print(f'Type "use {item_name.lower()}" to consume item.')
                    sealed_rooms.append(current_room)
                    unchosen = [i for i in available if i != item_name]

                    if unchosen:
                        print(f'The {unchosen[0]} disappears and you hear the room groan.')

                    else:
                        print('The room is now sealed behind you.')


# Notification of having collected required items


                    if items_collected >= 6:
                        print('You hear a distant rumble...\nThe Boss Room is now open...')
                        print('Princess Zelda is waiting. So is Ganon. I hope you are prepared.')

                    else:
                        print(f'Items collected: {items_collected} / 6 required.\nContinue your search.')

                elif available:
                    print(f'There is no {item_name} here.')
                    print(f' You may choose {available[0]} or {available[1]}')

                else:
                    print(f'There is no items left in this room.')


# Using an item


            if command.startswith('use '):
                item_name = command[4:].strip().title()
                sword_damage, damage_resist, player_hearts, = use_item(item_name, inventory, sword_damage, damage_resist, player_hearts)


            else:
                print('Invalid command. The winds of Hyrule do not understand that.')
                print('Commands: go [direction], get [item_name], use [item_name] or quit')


if __name__ == '__main__':
    main()