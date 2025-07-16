class Ale:
    def __init__(self, name, abv):
        self.name = name
        self.abv = abv

    def alcohol_content(self, volume_in_oz):
        return self.abv * volume_in_oz

    def description(self):
        return f"{self.name}: {self.abv * 100:.1f}% ABV"


class Blonde(Ale):
    def __init__(self):
        Ale.__init__(self, " Blonde ", 0.05)


class IPA(Ale):
    def __init__(self):
        Ale.__init__(self, "IPA", 0.06)


class Wheat(Ale):
    def __init__(self):
        Ale.__init__(self, "Wheat", 0.07)


class ScotchAle(Ale):
    def __init__(self):
        Ale.__init__(self, "Scotch Ale", 0.08)

#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  IF THERE IS ANY CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓         PLEASE DO NOT MODIFY IF       ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 