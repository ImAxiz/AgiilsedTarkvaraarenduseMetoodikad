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

    def attack(self, enemy):
        if self.energy > 5:
            self.energy -= 5
            damage = 10
            enemy.health -= damage
            print(f"Ründasid vastast! Tehtud kahju: {damage}")
        else:
            print("Ei ole piisavalt energiat rünnakuks!")

    def eat(self):
        if self.food > 0:
            self.food -= 1
            self.health += 5
            print("Sööd midagi! Tervis taastub.")
        else:
            print("Pole toitu, et süüa!")

    def move(self):
        if self.energy > 3:
            self.energy -= 3
            self.time_left -= 1
            print("Liikusid edasi! Aega jäänud vähenes.")
        else:
            print("Ei ole piisavalt energiat liikumiseks!")

def game_over(player):
    if player.health <= 0:
        print("Mängija on surnud. Mäng läbi!")
        return True
    elif player.time_left <= 0:
        print("Aeg on läbi! Mäng läbi.")
        return True
    return False

player = Player()
enemy = Player(health=50, food=2, energy=30, time_left=3)

while not game_over(player):
    print("Mängija tegevused:")
    player.show_status()
    
    action = input("Vali tegevus (rest, attack, eat, move): ").lower()

    if action == "rest":
        player.rest()
    elif action == "attack":
        player.attack(enemy)
    elif action == "eat":
        player.eat()
    elif action == "move":
        player.move()
    else:
        print("Vale tegevus, proovi uuesti.")
    
    if game_over(player):
        break
