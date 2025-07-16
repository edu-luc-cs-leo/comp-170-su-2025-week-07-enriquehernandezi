class Vehicle:
    def __init__(self, name, mpg):
        self.name = name
        self.mpg = mpg

    def fuel_needed(self, distance):
        return distance / self.mpg

    def description(self):
        return f"{self.name} gets {self.mpg} miles per gallon."


class Car(Vehicle):
    def __init__(self):
        Vehicle.__init__(self, "Car", 10)


class Bike(Vehicle):
    def __init__(self):
        Vehicle.__init__(self, "Bike", 20)


class Motorcycle(Vehicle):
    def __init__(self):
        Vehicle.__init__(self, "Motorcycle", 30)


class Train(Vehicle):
    def __init__(self):
        Vehicle.__init__(self, "Train", 40)

#Reflection
#1 Didn’t add comments, which hurts readability for others. Variable naming is good, but structure could use a bit more documentation.
#2 Didn’t check if the list was empty. Manually tracked count even though len() is simpler.
#3 Didn’t finish the function, missing the _ case, no check for non-alpha words, and didn’t print the final result.

#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  IF THERE IS ANY CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓         PLEASE DO NOT MODIFY IF       ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 