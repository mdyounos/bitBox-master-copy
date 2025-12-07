class Monster:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def attack(self):
        print(f"{self.name} is in Attacking Mode...")


class Fogthing(Monster):
    def make_sound(self):
        print("Geeeeeeeeeeeffffffffffff....\n")


class Mournsnake(Monster):
    def make_sound(self):
        print("Sssssssssssssssssssssssssssss....\n")


# Create objects
fogthing = Fogthing("Fogthing", "Yellow")
mournsnake = Mournsnake("Mournsnake", "Red")

# Call methods
fogthing.attack()
fogthing.make_sound()

mournsnake.attack()
mournsnake.make_sound()
