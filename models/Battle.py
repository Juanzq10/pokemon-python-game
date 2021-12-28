from models.Constants import * 

class Battle: 
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.actual_turn = 0
    
    def is_finished(self): 
        finished = self.pokemon1.current_hp <= 0 or self.pokemon2.current_hp <= 0

        if finished: 
            self.print_winner()
            
        return finished
    
    def execute_turn(self, turn): 
        command1 = turn.command1
        command2 = turn.command2
        attack1 = None
        attack2 = None 

        if DO_ATTACK in command1.action.keys(): 
            attack1 = self.pokemon1.attacks[command1.action[DO_ATTACK]]

        if DO_ATTACK in command2.action.keys():
            attack2 = self.pokemon2.attacks[command2.action[DO_ATTACK]]
        
        self.pokemon2.current_hp -= self.compute_damage(attack1, self.pokemon1, self.pokemon2)
        self.pokemon1.current_hp -= self.compute_damage(attack2, self.pokemon2, self.pokemon1)

        self.actual_turn += 1

    def compute_damage(self, attack, pokemon1, pokemon2): 
        aux = ((2 * pokemon1.level)/5) + 2
        power_factor = aux * attack.power

        if attack.type == PHYSICAL: 
            power_factor *= (pokemon1.stats[ATTACK] / pokemon2.stats[ATTACK])
        
        if attack.type == SPECIAL: 
            power_factor *= (pokemon1.stats[SPECIAL_ATTACK] / pokemon2.stats[SPECIAL_DEFENSE])

        damage_without_modifier = power_factor/50 + 2
        return damage_without_modifier * self.compute_damage_modifier(attack, pokemon1, pokemon2)
    
    def compute_damage_modifier(self, attack, pokemon1, pokemon2): 
        modifier = 1
        stab = 1
        if (attack.type == pokemon1.type1) or (attack.type == pokemon1.type2): 
            stab = 1.5

        modifier *= stab
        return modifier

    
    def print_current_status(self):
        print(self.pokemon1.name + ": " + str(self.pokemon1.current_hp) + " HP")
        print(self.pokemon2.name + ": " + str(self.pokemon2.current_hp) + " HP")

    def print_winner(self): 
        if self.pokemon1.current_hp <= 0 and self.pokemon2.current_hp > 0:
            print(self.pokemon2.name + " wins!")
        
        if self.pokemon2.current_hp <= 0 and self.pokemon1.current_hp > 0:
            print(self.pokemon1.name + " wins!")
        
        if self.pokemon1.current_hp <= 0 and self.pokemon2.current_hp <= 0:
            print("It's a draw!")
            
class Turn: 

    def __init__(self):
        self.command1 = None
        self.command2 = None

    def can_start(self):
        return self.command1 is not None and self.command2 is not None

class Command: 
    def __init__(self, action):
        self.action = action