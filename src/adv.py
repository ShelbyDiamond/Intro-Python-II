from src.room import Room

# Declare all the rooms
from src.player import Player

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
print()
print("********* WELCOME TO YOUR PRINCESS ADVENTURE GAME *********")
p_name = input("To get started, give your princess a name >>> ")
player = Player(p_name, room["outside"])
print(f"Make sure to look around, you may quit the game at any time by typing 'Q' and Good Luck {player.name}!")
print()
print(f"{player.name} is currently {player.current_room.name}. {player.current_room.description}")
print(f"Available items thrown across the ground:")
for i in room["outside"].items:
    print(f"\t{i}")


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

instructional_text = """
******************** Available Move Options ******************
**** { n } North | { s } South |  { w } West | { e } East ****
************** Enter [Q] to Exit the Adventure ***************
"""

print(instructional_text)
play_input = ""
while play_input != "Q":
    play_input = input("Make your move\n").upper()
    print(player.items)
    if play_input == 'N' or play_input == 'S' or play_input == 'E' or play_input == 'W':
        player.walk(play_input.lower())
    elif play_input.lower() == "grab":
        print("you said grab?!?!?!?!")
        player.get_item()
    elif play_input.lower() == "drop":
        print("..dropping..")
        player.drop_item()
    elif play_input == "Q":
        print(f'Safe travels, {player.name}! May you have long days and pleasant nights.\n')
        break