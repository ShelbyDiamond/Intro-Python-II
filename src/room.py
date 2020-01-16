# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def room_function(self):
        print(self.name, self.description)


class Direction(Room):
    def __init__(self, n_to, s_to, e_to, w_to, name, description):
        super().__init__(name, description)
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to

    def direction_function(self):
        print(self.n_to, self.s_to, self.e_to, self.w_to)