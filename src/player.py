# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, items, currentRoom)
        self.name = name
        self.items = items
        self.currentRoom = currentRoom


    def __str__(self):
    return f"{self.name} is in {self.currentRoom}"