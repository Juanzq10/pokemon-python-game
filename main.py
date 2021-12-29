from models.Constants import * 
from models.Battle import *
from models.Pokemon import *

pokemon1 = Pokemon("Bulbasaur", 78, GRASS, POISON)
pokemon2 = Pokemon("Charmander", 100, WATER, GROUND)

pokemon1.current_hp = 45
pokemon2.current_hp = 39

pokemon1.base_stats = {
    HP: 108,
    ATTACK: 130,
    DEFENSE: 95,
    SPECIAL_ATTACK: 80,
    SPECIAL_DEFENSE: 85,
    SPEED: 102
}

pokemon1.ev = {
    HP: 74,
    ATTACK: 190,
    DEFENSE: 91,
    SPECIAL_ATTACK: 48,
    SPECIAL_DEFENSE: 84,
    SPEED: 23
}

pokemon1.iv = {
    HP: 24,
    ATTACK: 12,
    DEFENSE: 30,
    SPECIAL_ATTACK: 16,
    SPECIAL_DEFENSE: 23,
    SPEED: 5
}

pokemon1.compute_stats()

pokemon2.base_stats = {
    HP: 39,
    ATTACK: 52,
    DEFENSE: 43,
    SPECIAL_ATTACK: 80,
    SPECIAL_DEFENSE: 65,
    SPEED: 65
}

pokemon2.ev = {
    HP: 74,
    ATTACK: 190,
    DEFENSE: 91,
    SPECIAL_ATTACK: 48,
    SPECIAL_DEFENSE: 84,
    SPEED: 23
}

pokemon2.iv = {
    HP: 31,
    ATTACK: 31,
    DEFENSE: 31,
    SPECIAL_ATTACK: 31,
    SPECIAL_DEFENSE: 31,
    SPEED: 31
}


pokemon1.attacks = [Attack("Scratch", GRASS, PHYSICAL, 10, 10, 100)]
pokemon2.attacks = [Attack("Scratch", FIRE, PHYSICAL, 10, 10, 100)]


def ask_command(pokemon): 
    command = None

    while not command:
        tmp_command = input("What should " + pokemon.name + " do? ").split(" ")

        if len(tmp_command) == 2:
            try: 
                if tmp_command[0] == DO_ATTACK and 0 <= int(tmp_command[1]) < 4:
                    command = Command({DO_ATTACK: int(tmp_command[1])}) 
            except Exception: 
                pass 
    return command

battle = Battle(pokemon1, pokemon2)

while not battle.is_finished(): 
    command1 = ask_command(pokemon1)
    command2 = ask_command(pokemon2)

    turn = Turn()
    turn.command1 = command1
    turn.command2 = command2

    if turn.can_start(): 
        battle.execute_turn(turn)
        battle.print_current_status()