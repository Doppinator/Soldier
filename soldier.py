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