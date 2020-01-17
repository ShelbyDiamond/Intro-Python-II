class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def __str__(self):
        return f"{self.name} {self.current_room}"

    def walk(self, direction):
        #  this will check if the current room has space to move into
        if getattr(self.current_room, f"{direction}_to") is not None:
            # if possible change to the desired room
            self.current_room = getattr(self.current_room, f"{direction}_to")
            # printing details of the new room
            print(f"\n{self.current_room.name}.\n{self.current_room.description}\nItems: {self.current_room.items}")

            # available items in that room
            print(f"Available items scattered across the ground:")
            # printing multiple items nicely
            for i in self.current_room.items:
                print(f"\t{i}")
        # if no path available show this message
        else:
            print(f"\nThere appears to be a wall in the way! TRY AGAIN\n")

    # get_item grabs items from the current room
    def get_item(self):
        if len(self.current_room.items) > 0:
            x = self.current_room.items.pop()
            self.items.append(x)
            print(self.items)
        # else show this message
        else:
            print("\nThere are no items left here, and you've doomed the universe. Way to go.\n")

    # drop_item drops the players list items
    def drop_item(self):
        if len(self.items) > 0:
            x = self.items.pop()
            self.current_room.items.append(x)
        else:
            print("\nYour pack is empty!\n")