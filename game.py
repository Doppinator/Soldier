from soldier import Soldier, Medic

def show_status():
    print("\n===== Soldiers =====")

    for soldier in soldiers.values():
        print(
            f"{soldier.name:<8}"
            f" HP:{soldier.health:<3}"
            f" Ammo:{soldier.ammo:<2}"
        )

def choose_soldier(prompt, current_player, soldiers):
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

soldiers = {
    "John": Soldier("John", 100, 30),
    "Dave": Soldier("Dave", 80, 50),
    "Kaya": Soldier("Kaya", 90, 40),
    "Medic": Medic("Medic", 85, 20)
}

turn_order = list(soldiers.values())
turn = 0

def run_game():
    global turn
    while True:
        current_player = turn_order[turn]
        show_status()
        print(f"\n===== {current_player.name}'s turn =====")
    
        enemy = choose_soldier(
        "Choose an enemy: ",
        current_player,
        soldiers
    )

        current_player.take_turn(enemy)
        turn = (turn + 1) % len(turn_order)