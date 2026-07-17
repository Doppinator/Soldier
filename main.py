from soldier import Soldier, Medic, show_status, choose_soldier 

soldiers = {
    "John": Soldier("John", 100, 30),
    "Dave": Soldier("Dave", 80, 50),
    "Kaya": Soldier("Kaya", 90, 40),
    "Medic": Medic("Medic", 85, 20)
}

turn_order = list(soldiers.values())
turn = 0



while True:
    current_player = turn_order[turn]
    show_status()
    print(f"\n===== {current_player.name}'s turn =====")

    current_player.take_turn()

    # Move to the next player
    turn = (turn + 1) % len(turn_order)
