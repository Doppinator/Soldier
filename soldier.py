class Soldier:
    def __init__(self, name, health, ammo):
        self.name = name
        self.health = health
        self.ammo = ammo
    
    def take_turn(self, enemy):
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

class Medic(Soldier):

    def heal(self, target):
        target.health += 20

        print(f"{self.name} heals {target.name}!")
        print(f"{target.name}'s health: {target.health}")
            
