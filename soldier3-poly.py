class Soldier:
    def __init__(self, name, health, ammo):
        self.name = name
        self.health = health
        self.ammo = ammo
    
    def take_turn(self):
        enemy = choose_soldier("Choose an enemy: ", self)
        self.shoot(enemy)

    def shoot(self, enemy):
        if self.ammo > 0:
            self.ammo -= 1
            enemy.health -= 10

            print(f"{self.name} shoots at {enemy.name}!")
            print(f"{self.name}'s ammo: {self.ammo}")
            print(f"{enemy.name}'s health: {enemy.health}")

            if enemy.health <= 0:
                print(f"{enemy.name} is already defeated!")
        else:
            print(f"{self.name} has no ammo left!")

def show_status():
    print("\n===== Soldiers =====")

    for soldier in soldiers.values():
        print(
            f"{soldier.name:<8}"
            f" HP:{soldier.health:<3}"
            f" Ammo:{soldier.ammo:<2}"
        )

class Medic(Soldier):

    def heal(self, target):
        target.health += 20

        print(f"{self.name} heals {target.name}!")
        print(f"{target.name}'s health: {target.health}")

    def take_turn(self):

        while True:

            action = input(
                "1. Shoot\n"
                "2. Heal\n"
            )

            if action == "1":
                super().take_turn()
                break

            elif action == "2":
                ally = choose_soldier("Choose a soldier to heal: ", self)
                self.heal(ally)
                break

            print("Invalid choice.")

soldiers = {
    "John": Soldier("John", 100, 30),
    "Dave": Soldier("Dave", 80, 50),
    "Kaya": Soldier("Kaya", 90, 40),
    "Medic": Medic("Medic", 85, 20)
}

turn_order = list(soldiers.values())
turn = 0

def choose_soldier(prompt, current_player):
    while True:
        name = input(prompt)

        if name not in soldiers:
            print("Invalid soldier.")
            continue

        chosen = soldiers[name]

        if chosen is current_player:
            print("You cannot choose yourself.")
            continue

        return chosen

while True:
    current_player = turn_order[turn]
    show_status()
    print(f"\n===== {current_player.name}'s turn =====")

    current_player.take_turn()

    # Move to the next player
    turn = (turn + 1) % len(turn_order)
