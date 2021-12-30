#Pokemon stats 
HP = "HP"
ATTACK = "ATTACK"
DEFENSE = "DEFENSE"
SPECIAL_ATTACK = "SPECIAL_ATTACK"
SPECIAL_DEFENSE = "SPECIAL_DEFENSE"
SPEED = "SPEED"


#Attack Categories
PHYSICAL = "Physical"
SPECIAL = "Special"

#Command Actions
DO_ATTACK = "Attack"
DO_ATTACK_SELECTION = "Selected_attack"


#Pokemon Types
GRASS = "Grass"
FIRE = "Fire"
WATER = "Water"
ELECTRIC = "Electric"
NORMAL = "Normal"
PSYCHIC = "Psychic"
ICE = "Ice"
DRAGON = "Dragon"
DARK = "Dark"
GHOST = "Ghost"
FIGHTING = "Fighting"
FLYING = "Flying"
POISON = "Poison"
GROUND = "Ground"
ROCK = "Rock"
BUG = "Bug"
STEEL = "Steel"
FAIRY = "Fairy"

TYPE_MAP = {
    "Grass": GRASS,
    "Fire": FIRE,
    "Water": WATER,
    "Electric": ELECTRIC,
    "Normal": NORMAL,
    "Psychic": PSYCHIC,
    "Ice": ICE,
    "Dragon": DRAGON,
    "Dark": DARK,
    "Ghost": GHOST,
    "Fighting": FIGHTING,
    "Flying": FLYING,
    "Poison": POISON,
    "Ground": GROUND,
    "Rock": ROCK,
    "Bug": BUG,
    "Steel": STEEL,
    "Fairy": FAIRY
} 

EFFECTIVENESS = {
    GRASS: {FIRE: 0.5, WATER: 2, ELECTRIC: 0.5, GRASS: 0.5, NORMAL: 1, PSYCHIC: 1, ICE: 1, DRAGON: 0.5, DARK: 1, GHOST: 1, FIGHTING: 1, FLYING: 0.5, POISON: 0.5, GROUND: 2, ROCK: 2, BUG: 0.5, STEEL: 0.5, FAIRY: 1},
    FIRE: {GRASS: 2, FIRE: 0.5, WATER: 0.5, ELECTRIC: 1, NORMAL: 1, PSYCHIC: 1, ICE: 2, DRAGON: 0.5, DARK: 1, GHOST: 1, FIGHTING: 1, FLYING: 1, POISON: 1, GROUND: 1, ROCK: 0.5, BUG: 2, STEEL: 2, FAIRY: 1},
    WATER: {GRASS: 0.5, FIRE: 2, WATER: 0.5, ELECTRIC: 1, NORMAL: 1, PSYCHIC: 1, ICE: 1, DRAGON: 0.5, DARK: 1, GHOST: 1, FIGHTING: 1, FLYING: 1, POISON: 1, GROUND: 2, ROCK: 2, BUG: 1, STEEL: 1, FAIRY: 1},
    ELECTRIC: {GRASS: 0.5, FIRE: 1, WATER: 2, ELECTRIC: 0.5, NORMAL: 1, PSYCHIC: 1, ICE: 1, DRAGON: 0.5, DARK: 1, GHOST: 1, FIGHTING: 1, FLYING: 2, POISON: 1, GROUND: 0, ROCK: 1, BUG: 1, STEEL: 1, FAIRY: 1},
    NORMAL: {GRASS: 1, FIRE: 1, WATER: 1, ELECTRIC: 1, NORMAL: 1, PSYCHIC: 1, ICE: 1, DRAGON: 1, DARK: 1, GHOST: 0, FIGHTING: 1, FLYING: 1, POISON: 1, GROUND: 1, ROCK: 0.5, BUG: 1, STEEL: 0.5, FAIRY: 1},
    PSYCHIC: {GRASS: 1, FIRE: 1, WATER: 1, ELECTRIC: 1, NORMAL: 1, PSYCHIC: 0.5, ICE: 1, DRAGON: 1, DARK: 0, GHOST: 1, FIGHTING: 2, FLYING: 1, POISON: 2, GROUND: 1, ROCK: 1, BUG: 1, STEEL: 0.5, FAIRY: 1},
    ICE: {GRASS: 1, FIRE: 0.5, WATER: 0.5, ELECTRIC: 1, NORMAL: 1, PSYCHIC: 1, ICE: 0.5, DRAGON: 2, DARK: 1, GHOST: 1, FIGHTING: 1, FLYING: 2, POISON: 1, GROUND: 2, ROCK: 1, BUG: 1, STEEL: 0.5, FAIRY: 1},
    DRAGON: {GRASS: 1, FIRE: 1, WATER: 1, ELECTRIC: 1, NORMAL: 1, PSYCHIC: 1, ICE: 1, DRAGON: 2, DARK: 1, GHOST: 1, FIGHTING: 1, FLYING: 1, POISON: 1, GROUND: 1, ROCK: 1, BUG: 1, STEEL: 0.5, FAIRY: 0},
    DARK: {GRASS: 1, FIRE: 1, WATER: 1, ELECTRIC: 1, NORMAL: 1, PSYCHIC: 2, ICE: 1, DRAGON: 1, DARK: 0.5, GHOST: 2, FIGHTING: 0.5, FLYING: 1, POISON: 1, GROUND: 1, ROCK: 1, BUG: 1, STEEL: 1, FAIRY: 0.5},
    GHOST: {GRASS: 1, FIRE: 1, WATER: 1, ELECTRIC: 1, NORMAL: 0, PSYCHIC: 2, ICE: 1, DRAGON: 1, DARK: 0.5, GHOST: 2, FIGHTING: 1, FLYING: 1, POISON: 1, GROUND: 1, ROCK: 1, BUG: 1, STEEL: 1, FAIRY: 1},
    FIGHTING: {GRASS: 1, FIRE: 1, WATER: 1, ELECTRIC: 1, NORMAL: 2, PSYCHIC: 0.5, ICE: 2, DRAGON: 1, DARK: 2, GHOST: 0, FIGHTING: 1, FLYING: 0.5, POISON: 0.5, GROUND: 1, ROCK: 2, BUG: 1, STEEL: 2, FAIRY: 0.5},
    FLYING: {GRASS: 2, FIRE: 1, WATER: 1, ELECTRIC: 0.5, NORMAL: 1, PSYCHIC: 1, ICE: 1, DRAGON: 1, DARK: 1, GHOST: 1, FIGHTING: 2, FLYING: 1, POISON: 1, GROUND: 1, ROCK: 0.5, BUG: 2, STEEL: 0.5, FAIRY: 1},
    POISON: {GRASS: 2, FIRE: 1, WATER: 1, ELECTRIC: 1, NORMAL: 1, PSYCHIC: 1, ICE: 1, DRAGON: 1, DARK: 1, GHOST: 0.5, FIGHTING: 1, FLYING: 1, POISON: 0.5, GROUND: 0.5, ROCK: 0.5, BUG: 0.5, STEEL: 0, FAIRY: 2},
    GROUND: {GRASS: 0.5, FIRE: 2, WATER: 1, ELECTRIC: 2, NORMAL: 1, PSYCHIC: 1, ICE: 1, DRAGON: 1, DARK: 1, GHOST: 1, FIGHTING: 1, FLYING: 0, POISON: 2, GROUND: 1, ROCK: 2, BUG: 0.5, STEEL: 2, FAIRY: 1},
    ROCK: {GRASS: 1, FIRE: 2, WATER: 1, ELECTRIC: 1, NORMAL: 1, PSYCHIC: 1, ICE: 1, DRAGON: 1, DARK: 1, GHOST: 1, FIGHTING: 0.5, FLYING: 2, POISON: 1, GROUND: 0.5, ROCK: 1, BUG: 2, STEEL: 0.5, FAIRY: 1},
    BUG: {GRASS: 2, FIRE: 0.5, WATER: 1, ELECTRIC: 1, NORMAL: 1, PSYCHIC: 2, ICE: 1, DRAGON: 1, DARK: 1, GHOST: 1, FIGHTING: 0.5, FLYING: 0.5, POISON: 0.5, GROUND: 1, ROCK: 1, BUG: 1, STEEL: 0.5, FAIRY: 0.5},
    STEEL: {GRASS: 1, FIRE: 0.5, WATER: 0.5, ELECTRIC: 0.5, NORMAL: 1, PSYCHIC: 1, ICE: 2, DRAGON: 1, DARK: 1, GHOST: 1, FIGHTING: 1, FLYING: 2, POISON: 1, GROUND: 1, ROCK: 2, BUG: 1, STEEL: 0.5, FAIRY: 2},
    FAIRY: {GRASS: 1, FIRE: 0.5, WATER: 1, ELECTRIC: 1, NORMAL: 1, PSYCHIC: 1, ICE: 1, DRAGON: 2, DARK: 2, GHOST: 1, FIGHTING: 2, FLYING: 1, POISON: 0.5, GROUND: 1, ROCK: 1, BUG: 1, STEEL: 0.5, FAIRY: 1}
}

#Pokemon Natures
HARDY = "Hardy"

NATURE_MAP = {
    HARDY: {HP: 1, ATTACK: 1.1, DEFENSE: 0.9, SPECIAL_ATTACK: 1, SPECIAL_DEFENSE: 1, SPEED: 1}
}
