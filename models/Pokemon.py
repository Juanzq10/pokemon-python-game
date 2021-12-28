from models.Constants import *

class Pokemon: 

    def __init__(self, name, level, type1, type2) -> None:
        self.name = name 
        self.level = level 
        self.type1 = type1
        self.type2 = type2
        self.attacks = []
        self.stats = {}
        self.base_stats = {}
        self.ev = {}
        self.iv = {}
        self.current_status = 0
        self.current_hp = 0
        self.nature = 0

    def is_dead(self):
        return self.current_hp <= 0

    def compute_stats(self):
        self.stats = {
            HP: self.compute_hp_stat(),
            ATTACK: self.compute_stantard_stat(ATTACK),
            DEFENSE: self.compute_stantard_stat(DEFENSE),
            SPECIAL_ATTACK: self.compute_stantard_stat(SPECIAL_ATTACK),
            SPECIAL_DEFENSE: self.compute_stantard_stat(SPECIAL_DEFENSE),
            SPEED: self.compute_stantard_stat(SPEED)
        } 

    def compute_stantard_stat(self, stat): 
        value = (2 * self.base_stats[stat] + self.iv[stat] + int(self.ev[stat] / 4)) * self.level
        return (int(value/100) + 5) * NATURE_MAP[HARDY][stat]
 
    def compute_hp_stat(self):
        value = (2 * self.base_stats[HP] + self.iv[HP] + int(self.ev[HP] / 4)) * self.level 
        return int(value/100) + self.level + 10
        
class Attack: 

    def __init__(self, name, t, category, PP, power, accuracy) -> None:
        self.name = name 
        self.type = t
        self.category = category
        self.PP = PP
        self.power = power
        self.accuracy = accuracy