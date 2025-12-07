class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
        self._pineapple_allowed = False

    @property
    def pineapple_allowed(self):
        return self._pineapple_allowed

    @pineapple_allowed.setter
    def pineapple_allowed(self, value):
        if value:  # Asking to enable pineapple
            password = input("Enter the Password: ")
            if password == "Brownfish1":
                self._pineapple_allowed = value
            else:
                raise ValueError("Alert! Unauthorized!")
        else:
            # Allow disabling without a password
            self._pineapple_allowed = False


pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)

pizza.pineapple_allowed = True  # <-- ask for password
print(pizza.pineapple_allowed)
