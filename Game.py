from models.Battle import *
from models.Button import Button
from models.Constants import *
import pygame 
from pygame.locals import *
from models.Pokemon import *
import json

class Game: 

    def print_hola(self):
        print("Hola")

    def __init__(self):
        self.buttons = [Button(500, 500, 100, 40, "Attack", self.print_hola)]
        pygame.init()

        self.screen = pygame.display.set_mode((160 * 4, 144 * 4))
        pygame.display.set_caption("Pokemon Battle")

        clock = pygame.time.Clock()
        clock.tick(60)

        self.pokemon1 = Pokemon("Bulbasaur", 78, GRASS, POISON)
        self.pokemon2 = Pokemon("Bulbasaur", 100, GRASS, POISON)
        self.init_pokemon_stats() 

        self.pokemon1.attacks = [Attack("Scratch", GRASS, PHYSICAL, 10, 10, 100)]
        self.pokemon2.attacks = [Attack("Scratch", FIRE, PHYSICAL, 10, 10, 100)]

        self.load_resources()

        self.battle = Battle(self.pokemon1, self.pokemon2)

        self.stopped = False

    def process(self): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stopped = True
            
            for button in self.buttons: 
                button.handle_event(event, self)

    def load_resources(self): 
        self.load_pokemon_image(self.pokemon1, True)
        self.load_pokemon_image(self.pokemon2, False)

    def load_pokemon_image(self, pokemon, is_player):
        pokemon_name = pokemon.name.lower()

        if is_player: 
            pokemon_img = pygame.image.load("resources/pokemon/" + pokemon_name + "_back.png")
        else: 
            pokemon_img = pygame.image.load("resources/pokemon/" + pokemon_name + "_front.png")
    
        pokemon_img = pygame.transform.scale(pokemon_img, (400, 400))
        pokemon.renderer = pokemon_img
    
    def render_pokemons(self): 
        self.pokemon1.render(self.screen, (10, 200))
        self.pokemon2.render(self.screen, (440, 0))

    def render_buttons(self):
        for button in self.buttons: 
            button.render(self)
    
    def render(self):
        self.screen.fill((255, 255, 255))
        self.render_pokemons()
        self.render_buttons()
        pygame.display.update()

    def make_turn(self):
        turn = Turn()
        turn.command1 = Command({DO_ATTACK: 0})

    def init_pokemon_stats(self):
        pokemon1 = "Bulbasaur"
        pokemon2 = "Bulbasaur"

        with open("pokemon_database/pokemons.json") as file: 
            data = json.load(file) 
            pokemon1_type2 = self.compute_type2(pokemon1)
            pokemon2_type2 = self.compute_type2(pokemon2)

            self.pokemon1 = Pokemon(pokemon1, 100, data[pokemon1]["type1"], pokemon1_type2)
            self.pokemon2 = Pokemon(pokemon2, 100, data[pokemon2]["type1"], pokemon2_type2)

            self.pokemon1.base_stats = {
                HP: data[self.pokemon1.name]["hp"],
                ATTACK: data[self.pokemon1.name]["attack"],
                DEFENSE: data[self.pokemon1.name]["defense"],
                SPECIAL_ATTACK: data[self.pokemon1.name]["sp_attack"],
                SPECIAL_DEFENSE: data[self.pokemon1.name]["sp_defense"],
                SPEED: data[self.pokemon1.name]["speed"]
            }

            self.pokemon2.base_stats = {
                HP: data[self.pokemon2.name]["hp"],
                ATTACK: data[self.pokemon2.name]["attack"],
                DEFENSE: data[self.pokemon2.name]["defense"],
                SPECIAL_ATTACK: data[self.pokemon2.name]["sp_attack"],
                SPECIAL_DEFENSE: data[self.pokemon2.name]["sp_defense"],
                SPEED: data[self.pokemon2.name]["speed"]
            }

            self.pokemon1.ev = {
                HP: 0,
                ATTACK: 0,
                DEFENSE: 0,
                SPECIAL_ATTACK: 0,
                SPECIAL_DEFENSE: 0,
                SPEED: 0
            }

            self.pokemon2.ev = {
                HP: 0,
                ATTACK: 0,
                DEFENSE: 0,
                SPECIAL_ATTACK: 0,
                SPECIAL_DEFENSE: 0,
                SPEED: 0
            }

            self.pokemon1.iv = {
                HP: 21, 
                ATTACK: 21,
                DEFENSE: 21,
                SPECIAL_ATTACK: 21,
                SPECIAL_DEFENSE: 21,
                SPEED: 21
            }

            self.pokemon2.iv = {
                HP: 21, 
                ATTACK: 21,
                DEFENSE: 21,
                SPECIAL_ATTACK: 21,
                SPECIAL_DEFENSE: 21,
                SPEED: 21
            }

            self.pokemon1.compute_stats()
            self.pokemon2.compute_stats()

            self.pokemon1.current_hp = self.pokemon1.stats[HP]
            self.pokemon2.current_hp = self.pokemon2.stats[HP]
    
    def compute_type2(self, pokemon_name): 
        with open("pokemon_database/pokemons.json") as file: 
            data = json.load(file) 
            type2 = None
            
            if "type2" in data[pokemon_name].keys(): 
                type2 = data[pokemon_name]["type2"]
                type2 = TYPE_MAP[type2]
            
            return type2

game = Game() 
game.compute_type2("Blastoise")
