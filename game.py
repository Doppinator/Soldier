enemy = choose_soldier(
    "Choose an enemy: ",
    current_player,
    soldiers
)

current_player.take_turn(enemy)

