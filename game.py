from soldier import Soldier, Medic

def show_status(soldiers):
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

def handle_player_turn(player, soldiers):
    action = input("Choose an action (shoot/heal): ").strip().lower()
    perform_action(player, action, choose_soldier("Choose a target: ", player, soldiers))

def perform_action(player, action, target):
    if action == "shoot":
        player.shoot(target)
    elif action == "heal" and isinstance(player, Medic):
        player.heal(target)
    else:
        print("Invalid action.")

def run_game():
    turn_order = list(soldiers.values())
    turn = 0
    while True:
        current_player = turn_order[turn]
        show_status(soldiers)
        print(f"\n===== {current_player.name}'s turn =====")

        handle_player_turn(current_player, soldiers)
    
        turn = (turn + 1) % len(turn_order)