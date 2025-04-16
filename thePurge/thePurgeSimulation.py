class Player:
    def __init__(self, health=100, food=3, energy=50, time_left=5):
        self.health = health
        self.food = food
        self.energy = energy
        self.time_left = time_left

    def rest(self):
        if self.food > 0:
            self.food -= 1
            self.energy += 10
            print("Puhkasid edukalt! +10 energiat.")
        else:
            print("Pole piisavalt toitu puhkamiseks.")
        self.time_left -= 1

    def show_status(self):
        print(f"Tervis: {self.health}")
        print(f"Toit: {self.food}")
        print(f"Energia: {self.energy}")
        print(f"Aega jäänud: {self.time_left}")
        print("-" * 20)

    def test_rest_function(self):
        print("Loome mängija")
        player = Player()

        print("Enne puhkust:")
        player.show_status()

        print("Teeme puhke:")
        player.rest()

        print("Pärast puhkust:")
        player.show_status()

player = Player()
player.test_rest_function()
