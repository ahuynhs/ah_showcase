import random
import copy

class Pokemon:
    """
    PURPOSE:
    define a class, Pokemon, that contains all the characteristics (or functions to get the characteristics) of your Pokemon
    
    EXPECTATIONS:
    user passes in a poke_type, a name for his/her pokemon (optional), and pokemon level, and a Pokemon class will be returned
    
    PARAMETERS:
    poke_type (str): your pokemon type. Can only be a poke_type from this list ["Squirtle", "Psyduck", "Staryu", "Seel", 
                                                                               "Charmander", "Vulpix", "Ponyta", "Growlithe",
                                                                               "Bulbasaur", "Bellsprout", "Exeggcute", "Tangela"]
    name      (str): custom name for your Pokemon. Default is set to None as this argument is optional.
    level     (int): level of your Pokemon. Default is set to 1.
    
    FUNCTIONS:
    rename_pokemon()        : renames the custom name of your Pokemon
    get_hp()                : gets max hp according to the level of your Pokemon
    get_total_experience()  : gets max experience (experience denominator) according to the level of your Pokemon 
    get_move_dmg()          : gets damage for every move in Pokemon move_list according to the level of your Pokemon
    level_up_from_exp()     : if Pokemon experience >= max experience, then Pokemon level will increase by 1
    """
    def __init__(self, poke_type, name=None, level=1):
        if name == None or name =="None":
            self.name = poke_type
        else:
            self.name = str(name)
        self.poke_type = poke_type
        self.level = level
        self.affection = 0
        self.experience = 0
        self.experience_total = self.get_total_experience()
        self.hp = self.get_hp()
        
        self.water_pokemon = ["Squirtle", "Psyduck", "Staryu", "Seel"]
        self.fire_pokemon = ["Charmander", "Vulpix", "Ponyta", "Growlithe"]
        self.grass_pokemon = ["Bulbasaur", "Bellsprout", "Exeggcute", "Tangela"]
        
        if self.poke_type in self.water_pokemon:
            self.type = "Water"
                            # format of the move_list dict is move: (attack damage, move count)
            self.move_list = {"BUBBLE": [20, 5], "WATER GUN": [20, 5],
                              "WATER PULSE": [30, 5], "HYDRO CANNON": [40, 3]}
        elif self.poke_type in self.fire_pokemon:
            self.type = "Fire"
            self.move_list = {"FLAMETHROWER": [20, 5], "FIRE SPIN": [20, 5],
                              "EMBER": [30, 5], "FLAME WHEEL": [40, 3]}
        elif self.poke_type in self.grass_pokemon:
            self.type = "Grass"
            self.move_list = {"VINE WHIP": [20, 5], "RAZOR LEAF": [20, 5], 
                              "BULLET SEED": [30, 5], "LEAFAGE": [40, 3]}
        
        self.move_list_copy = copy.deepcopy(self.move_list)
        self.pokemon_dict = self.get_pokemon_stats()
        self.get_move_dmg()
    
    def rename_pokemon(self, name):
        if name == None or name == "None":
            self.name = self.poke_type
        else:
            self.name = str(name)
        
    def get_hp(self):
        # code to get hp based on level
        if self.level >= 1 and self.level <= 5:
            self.hp = 150
        elif self.level >= 6 and self.level <= 10:
            self.hp = 200
        elif self.level >= 11 and self.level <= 15:
            self.hp = 250
        elif self.level >= 16 and self.level <= 20:
            self.hp = 300
        elif self.level >= 21 and self.level <= 25:
            self.hp = 350
        elif self.level >= 26 and self.level <= 30:
            self.hp = 400
        elif self.level >= 31 and self.level <= 35:
            self.hp = 450
        else:
            self.hp = 500
        return self.hp
    
    def get_total_experience(self):
        # code to  change the experience_total; with every level up, the experience level goes up by 20
        if self.level == 1:
            self.experience_total = 100
        else:
            self.experience_total = 100 + (20*self.level) # with every level up, the experience level goes up by 20
        return self.experience_total
    
    def get_move_dmg(self):
        # code to increase the damage of moves based on level
        if self.level >= 1 and self.level <= 5:
            increase = 0
        elif self.level >= 6 and self.level <= 10:
            increase = 3
        elif self.level >= 11 and self.level <= 15:
            increase = 6
        elif self.level >= 16 and self.level <= 20:
            increase = 9
        elif self.level >= 21 and self.level <= 25:
            increase = 12
        elif self.level >= 26 and self.level <= 30:
            increase = 15
        elif self.level >= 31 and self.level <= 35: 
            increase = 18
        elif self.level == 36: # no more move power increases after level 36
            increase = 21
        else:
            increase = 0
        
        for move in self.move_list:
            self.move_list[move][0] = self.move_list_copy[move][0] + increase
            
        return self.move_list
        
    def level_up_from_exp(self):
        # code to level up
        if self.experience/self.experience_total >= 1:
            self.level += 1
            print("{} just grew to level {}!".format(self.name, self.level))
            self.hp = self.get_hp()
            self.experience_total = self.get_total_experience()
            self.move_list = self.get_move_dmg()
            for move in self.move_list:
                self.move_list[move][1] = self.move_list_copy[move][1]
#             self.move_list_copy = copy.deepcopy(self.move_list)
            self.experience = 0
        else:
            print("You need {} more more experience points to level up!".format(self.experience_total-self.experience))
            
    def get_pokemon_stats(self):
        self.pokemon_dict = {"name": self.name, "type": self.type, "hp": self.hp, "level": self.level,
                        "experience": str(self.experience)+"/"+str(self.experience_total), 
                        "affection": self.affection, "moves": self.move_list} 
        return self.pokemon_dict
    
    def __str__(self):
        self.pokemon_dict = self.get_pokemon_stats()
        st_list = "\nHere are your current Pokemon Stats!\n" + "------------\n"
        for key, value in self.pokemon_dict.items():
            st_list += (str(key+": ") + str(value) +"\n") 
        return st_list
    
    def __repr__(self):
        self.pokemon_dict = self.get_pokemon_stats()
        st_list = "\nHere are your current Pokemon Stats!\n" + "------------\n"
        for key, value in self.pokemon_dict.items():
            st_list += (str(key+": ") + str(value) +"\n") 
        return st_list

class Play:
    """
    PURPOSE:
    define a class, Play, that contains all the functionality to play with your Pokemon
    
    EXPECTATIONS:
    user passes in a Pokemon class and a Play class will be returned; returned play class will have a play_time function that 
    will increase user's Pokemon's affection
    
    PARAMETERS:
    our_pokemon (class): your Pokemon class. Refer to Pokemon class docstring to understand this class more
    
    FUNCTIONS:
    play_time()             : given a game (TAG, TICKLE, HIDE N'SEEK) and a Pokemon class, user will "play" with his/her Pokemon.
                              HP and affection will be changed accordingly to which game was selected. 
                              Calls level_up_from_affection() after every play_time.
                   
    level_up_from_affection(): If affection level is 100, there is 5% chance of increasing the level of user's Pokemon by 1.
    """
    
    def __init__(self, our_pokemon):
        game = str(input("Please choose a game: Tickle, Tag, Hide n' Seek.\n")).lower()
        
        while game not in ["tag", "tickle", "hide n' seek"]:
            print("{} is not an applicable game.".format(game))
            game = str(input("Please choose a game: Tickle, Tag, Hide n' Seek.\n")).lower()
        
        self.game = game
        
        self.play_time(our_pokemon)
    def play_time(self, our_pokemon):
        if self.game == "tickle" and our_pokemon.hp >= 15:
            our_pokemon.hp -= 15
            our_pokemon.affection += 5
            if our_pokemon.affection >= 100:
                our_pokemon.affection = 100
                print("\nCongratulations you have reached max level of affection!\n")
            print("\nYou play a round of tickle with your {}! {} wants to be the Tickle Monster next time!"\
                  .format(our_pokemon.name, our_pokemon.name))
            self.level_up_from_affection(our_pokemon)
            
        elif self.game == "tag" and our_pokemon.hp >= 30:
            our_pokemon.hp -= 30
            our_pokemon.affection += 15
            if our_pokemon.affection >= 100:
                our_pokemon.affection = 100
                print("\nCongratulations you have reached max level of affection!\n")
            print("\nYou play a round of tag with your {}! {} is going to be it next time!"\
                  .format(our_pokemon.name, our_pokemon.name))
            self.level_up_from_affection(our_pokemon)
            
        elif self.game == "hide n' seek" and our_pokemon.hp >= 60:
            our_pokemon.hp -= 60
            our_pokemon.affection += 25
            if our_pokemon.affection >= 100:
                our_pokemon.affection = 100
                print("\nCongratulations you have reached max level of affection!\n")
            print("\nYou play a round of hide n' seek with your {}! {} can hide so well!"\
                  .format(our_pokemon.name, our_pokemon.name))
            self.level_up_from_affection(our_pokemon)
            
        else:
            print("""\nYou don't have enough HP to play the game you want.\nWe are sending you to the Pokemon Center.
            \n. . .\n\n""")
            pc = Pokemon_Center(our_pokemon)

    def level_up_from_affection(self, our_pokemon):
        # there is a 5% chance of leveling up from max affection denoated by the following list
        chance = [0]*95 + [1]*5 # this is not denoted as a self variable because chance will not be used outside this function
        
        if random.choice(chance) == 1 and our_pokemon.affection == 100:
            our_pokemon.level += 1
            print("\n{} just grew to level {}!".format(our_pokemon.name, our_pokemon.level))
            our_pokemon.hp = our_pokemon.get_hp()
            our_pokemon.experience_total = our_pokemon.get_total_experience()
            our_pokemon.experience = 0
        print("\n{} had fun playing with you! Play with {} again soon!".format(our_pokemon.name, our_pokemon.name))        
        
    
class Pokemon_Center:
    """
    PURPOSE:
    define a class, Pokemon_Center, that contains all the functionality of healing your Pokemon / restoring move stats.
    
    EXPECTATIONS:
    user passes in a Pokemon Class, and a Pokemon_Center class is returned; returned class contains a function, heal_pokemon()
    that restores user's Pokemon's hp and move_list stats 
    
    PARAMETERS:
    our_pokemon (class): your Pokemon class. Refer to Pokemon class docstring to understand this class more
    
    FUNCTIONS:
    heal_pokemon()        : restores Pokemon's hp and move counts for every move in Pokemon's move_list
    """
    
    def __init__(self, our_pokemon):
        action = str(input("Hello!\nWelcome to our Pokémon Center.\nWe can heal your Pokémon to perfect health."+
                        "Would you like us to heal your Pokemon today?\nPlease input Yes or No.\n")).lower()
        
        while action not in ["yes", "no"]:
            print("\nSorry, we did not understand your choice.\n")
            action = str(input("Hello!\nWelcome to our Pokémon Center.\nWe can heal your Pokémon to perfect health."+
                        "Would you like us to heal your Pokemon today?\nPlease input Yes or No.\n")).lower()
        
        if action == "yes":
            self.pokemon_dict_original = our_pokemon.pokemon_dict.copy()
            self.heal_pokemon(our_pokemon)
            self.pokemon_dict = our_pokemon.get_pokemon_stats()
            print(self.__str__())
        else:
            print("\nThank you for visiting! We hope to see you again.")
        
    def heal_pokemon(self, our_pokemon):
        our_pokemon.hp = our_pokemon.get_hp()
        for move in our_pokemon.move_list:
            our_pokemon.move_list[move][1] = our_pokemon.move_list_copy[move][1]

    def __str__(self):
#         st_list = "Hello!\nWelcome to our Pokémon Center.\nWe can heal your Pokémon to perfect health.\n"
        st_list = "\n. . .\nOk, may I see your Pokémon?\n. . .\nThank you for waiting.\n"
        st_list += "Your Pokémon are fully healed.\nWe hope to see you again.\n"
        st_list += "\n------------\nThese are your original Pokemon Stats:\n"
        for key, value in self.pokemon_dict_original.items():
            st_list += (str(key+": ") + str(value) +"\n") 
        st_list += "\nThese are your updated Pokemon Stats:\n"
        for key, value in self.pokemon_dict.items():
            st_list += (str(key+": ") + str(value) +"\n") 
        return st_list
    
    def __repr__(self):
        st_list = "Ok, may I see your Pokémon?\n. . .\nThank you for waiting.\n"
        st_list += "Your Pokémon are fully healed.\nWe hope to see you again.\n"
        st_list += "\n------------\nThese were your original Pokemon Stats:\n"
        for key, value in self.pokemon_dict_original.items():
            st_list += (str(key+": ") + str(value) +"\n") 
        st_list += "\n------------\nThese are your updated Pokemon Stats:\n"
        for key, value in self.pokemon_dict.items():
            st_list += (str(key+": ") + str(value) +"\n") 
        return st_list

class Battle:
    """
    PURPOSE:
    define a class, Battle, that contains all the functionality creating a random Pokemon class to go against user's inputted
    Pokemon class.
    
    EXPECTATIONS:
    user passes in a Pokemon Class, and a random Pokemon class (WildPokemon) will be generated to become user's Pokemon's
    opponent as well as a battle class that contains a function, attack, that will allow user's Pokemon and random Pokemon
    to "fight" against each other
    
    PARAMETERS:
    our_pokemon (class): your Pokemon class. Refer to Pokemon class docstring to understand this class more
    
    FUNCTIONS:
    attack()        : takes inputted Pokemon Class and the random generated Pokemon class and has the two battle against each 
                      other based on the respective move_list in each Pokemon class. If a Pokemon is a "counter" type then 
                      one of the classes will have its move damage doubled for every move in the move_list. If the move, Flee,
                      is selected, there is a 50% chance of breaking out of this function.
    """
    def __init__(self, our_pokemon):
        self.wild_pokemon = ["Squirtle", "Psyduck", "Staryu", "Seel",
                              "Charmander", "Vulpix", "Ponyta", "Growlithe",
                              "Bulbasaur", "Bellsprout", "Exeggcute", "Tangela"]
        self.poke_level_ranges = [lev for lev in range(our_pokemon.level-5, our_pokemon.level+5) if lev >= 1]
        
        wild_poke_type = random.choice(self.wild_pokemon)
        wild_poke_level = random.choice(self.poke_level_ranges)
        self.WildPokemon = Pokemon(poke_type=wild_poke_type, name=None, level=wild_poke_level)
        
        self.attack(our_pokemon)
        
    def attack(self, our_pokemon):
        fainted_pokemon = 0
        print("\n{} has encountered a level {} wild {}!\n".format(our_pokemon.name, self.WildPokemon.level,\
                                                                  self.WildPokemon.name))
        while fainted_pokemon == 0:
            if sum([moves[1] for moves in our_pokemon.move_list.values()]) == 0:
                print("You have run out of available attack moves. Automatically selecting 'FLEE'.")
                move = "FLEE"
            else:
                move = str(input("Please choose one of the following moves: {}\n".format(\
                   [move for move in our_pokemon.move_list.keys() if our_pokemon.move_list[move][1] >= 1]+["FLEE"]))).upper()
            
            while move not in [move for move in our_pokemon.move_list.keys()]+["FLEE"] or (move in our_pokemon.move_list.keys()\
                                                                                and our_pokemon.move_list[move][1] < 1):
                print("\nYou have selected an unavailable move.\n")
                move = str(input("Please choose one of the following moves: {}\n".format(\
                [move for move in our_pokemon.move_list.keys() if our_pokemon.move_list[move][1] >= 1]+["FLEE"]))).upper()
                
            
            if our_pokemon.type == "Water" and self.WildPokemon.type == "Fire":
                # we will multiply our damage by poke_counter, so if we counter our opponent, poke_counter will = 1.5
                poke_counter = 1.5
            elif our_pokemon.type == "Fire" and self.WildPokemon.type == "Grass":
                poke_counter = 1.5
            elif our_pokemon.type == "Grass" and self.WildPokemon.type == "Water":
                poke_counter = 1.5
            else:
                poke_counter = 1
            
            if our_pokemon.type == "Water" and self.WildPokemon.type == "Grass":
                 # we will multiply wild pokemon damage by wild_counter, so if wild counters our pokemon, wild_counter will = 1.5
                wild_counter = 1.5
            elif our_pokemon.type == "Fire" and self.WildPokemon.type == "Water":
                wild_counter = 1.5
            elif our_pokemon.type == "Grass" and self.WildPokemon == "Fire":
                wild_counter = 1.5
            else:
                wild_counter = 1
                
            if move == "FLEE":
                chance = ["yes", "no"]
                flee_success = random.choice(chance)
                if flee_success == "yes":
                    break
                else:
                    print("You have failed to flee!")
                    
                    if sum([moves[1] for moves in self.WildPokemon.move_list.values()]) == 0:
                        wild_damage = 0
                    else:
                        wild_moves = [move for move in self.WildPokemon.move_list.keys()]
                        wild_move = random.choice(wild_moves)

                        if self.WildPokemon.move_list[wild_move][1] < 1:
                            wild_moves.remove(wild_move)
                            wild_move = random.choice(wild_move)

                        if self.WildPokemon.hp > 0:
                            wild_damage = self.WildPokemon.move_list[wild_move][0]*wild_counter
                            self.WildPokemon.move_list[wild_move][1] -= 1
                            print("\n{} used {}.\nInflicted {} damage to {}!".format(self.WildPokemon.name, wild_move, 
                                                                    wild_damage, our_pokemon.name))
                            our_pokemon.hp -= wild_damage
                            if our_pokemon.hp < 0:
                                our_pokemon.hp = 0
                            print("{} currently has {} hp!\n".format(our_pokemon.name, our_pokemon.hp))
            else:
                damage = our_pokemon.move_list[move][0]*poke_counter
                our_pokemon.move_list[move][1] -= 1
                print("\n{} used {}.\nInflicted {} damage to {}!".format(our_pokemon.name, move, 
                                                        damage, self.WildPokemon.name))
                self.WildPokemon.hp -= damage
                if self.WildPokemon.hp < 0:
                    self.WildPokemon.hp = 0
                print("{} currently has {} hp!\n".format(self.WildPokemon.name, self.WildPokemon.hp))
            
                if sum([moves[1] for moves in self.WildPokemon.move_list.values()]) == 0:
                    wild_damage = 0
                else:
                    wild_moves = [move for move in self.WildPokemon.move_list.keys()]
                    wild_move = random.choice(wild_moves)

                    if self.WildPokemon.move_list[wild_move][1] < 1:
                        wild_moves.remove(wild_move)
                        wild_move = random.choice(wild_move)
                    if self.WildPokemon.hp > 0:
                        wild_damage = self.WildPokemon.move_list[wild_move][0]*wild_counter
                        self.WildPokemon.move_list[wild_move][1] -= 1
                        print("\n{} used {}.\nInflicted {} damage to {}!".format(self.WildPokemon.name, wild_move, 
                                                                wild_damage, our_pokemon.name))
                        our_pokemon.hp -= wild_damage

                        if our_pokemon.hp < 0:
                            our_pokemon.hp = 0
                        print("{} currently has {} hp!\n".format(our_pokemon.name, our_pokemon.hp))
            
            if self.WildPokemon.hp <= 0:
                fainted_pokemon += 1
            if our_pokemon.hp <= 0:
                fainted_pokemon += 1
        
        if our_pokemon.hp >= self.WildPokemon.hp and move != "FLEE":
            print("\n{} has defeated {}. {} has gained 25 experience points!".format(\
                                                        our_pokemon.name, self.WildPokemon.name, our_pokemon.name))
            our_pokemon.experience += 25
            our_pokemon.level_up_from_exp()
            print(our_pokemon)
        elif move == "FLEE":
            print("We have successfully fled!")
        else:
            print("{} has defeated {}. Sending {} to the Pokemon center.\n".format(\
                                                        self.WildPokemon.name, our_pokemon.name, our_pokemon.name))
            pc = Pokemon_Center(our_pokemon)
            
class GameTime():
    """
    PURPOSE:
    define a class, GameTime, that essentially calls a class from above to performs that class's functionality
    
    EXPECTATIONS:
    user passes in an input of what "activity" they would like to do, and that activity's class will be called
    
    FUNCTIONS:
    starter_pokemon()   : "game" starts by having user select a starter Pokemon (can only be Squirtle, Charmander, or
                          Bulbasaur). A Pokemon class of that selected starter Pokemon type will be called.
    
    play_game()         : based on user's input, that corresponding class will be called so that the activity can be performed
    """
    def __init__(self):
        print("""Thank you for choosing to play Pokemon Trainer!\n
        To quit the game at any time, just enter the command: 'QUIT', when prompted
        to enter what you want to do in the game.\n""")
        
        self.starter_pokemon()
        self.play_game()
        
        
    def starter_pokemon(self):
        print("We will now begin by choosing your starter Pokemon.\n")
        starter_pokemon = str(input("Please pick from the three options: 'Squirtle', 'Charmander', or 'Bulbasaur'.\n")).capitalize()
        
        while starter_pokemon not in ["Squirtle", "Charmander", "Bulbasaur"]:
            print("\nYou have selected an unavailable Pokemon.\n")
            starter_pokemon = str(input("Please pick from the three options: 'Squirtle', 'Charmander', or 'Bulbasaur'.\n")).capitalize()
            
        print("\nCongratulations on choosing {}! Would you like to name your Pokemon?\n".format(starter_pokemon))
        
        naming = str(input("Yes or no?\n")).capitalize()
        
        while naming not in ["Yes", "No"]:
            print("\nSorry, we did not understand that. Would you like to name your Pokemon?\n")
            naming = str(input("Yes or no?\n")).capitalize()
    
        if naming == "Yes":
            custom_name = str(input("\nWhat would you like to name your Pokemon?\n"))
        else:
            custom_name = None
        
        self.our_pokemon = Pokemon(poke_type=starter_pokemon, name=custom_name, level=1)
        print(self.our_pokemon)
    
    def play_game(self):
        
        game_choice = str(input("\nWhat would you like to do with {}?\n".format(self.our_pokemon.name)+
                "Please choose from the following game options:\n"+
                "['RENAME POKEMON', 'GET POKEMON STATS', 'PLAY', 'BATTLE', 'POKEMON CENTER', 'QUIT']\n")).upper()
        
        while game_choice != "QUIT":
            while game_choice not in ['RENAME POKEMON', 'GET POKEMON STATS', 'PLAY',\
                                      'BATTLE', 'POKEMON CENTER', 'QUIT']:
                print("You have selected an unavailable option.")
                
                game_choice = str(input("\nWhat would you like to do with {}?\n".format(self.our_pokemon.name)+
                "Please choose from the following game options:\n"+
                "['RENAME POKEMON', 'GET POKEMON STATS', 'PLAY', 'BATTLE', 'POKEMON CENTER', 'QUIT']\n")).upper()
                
            if game_choice == "RENAME POKEMON":
                new_name = str(input("\nWhat would you like to rename your Pokemon?\n")).capitalize()
                while new_name == "":
                    new_name = str(input("\nWhat would you like to rename your Pokemon?\n")).capitalize()
                self.our_pokemon.rename_pokemon(new_name)
                print("\nOur Pokemon name is now: {}\n".format(self.our_pokemon.name))
                
                game_choice = str(input("\nWhat would you like to do with {}?\n".format(self.our_pokemon.name)+
                "Please choose from the following game options:\n"+
                "['RENAME POKEMON', 'GET POKEMON STATS', 'PLAY', 'BATTLE', 'POKEMON CENTER', 'QUIT']\n")).upper()

            elif game_choice == "GET POKEMON STATS":
                print(self.our_pokemon)
                
                game_choice = str(input("\nWhat would you like to do with {}?\n".format(self.our_pokemon.name)+
                "Please choose from the following game options:\n"+
                "['RENAME POKEMON', 'GET POKEMON STATS', 'PLAY', 'BATTLE', 'POKEMON CENTER', 'QUIT']\n")).upper()

            elif game_choice == "PLAY":
                play = Play(self.our_pokemon)
                
                print("\n{}'s affection is now: {}".format(self.our_pokemon.name, self.our_pokemon.affection))
                
                game_choice = str(input("\nWhat would you like to do with {}?\n".format(self.our_pokemon.name)+
                "Please choose from the following game options:\n"+
                "['RENAME POKEMON', 'GET POKEMON STATS', 'PLAY', 'BATTLE', 'POKEMON CENTER', 'QUIT']\n")).upper()

            elif game_choice == "BATTLE":
                battle = Battle(self.our_pokemon)
                
                game_choice = str(input("\nWhat would you like to do with {}?\n".format(self.our_pokemon.name)+
                "Please choose from the following game options:\n"+
                "['RENAME POKEMON', 'GET POKEMON STATS', 'PLAY', 'BATTLE', 'POKEMON CENTER', 'QUIT']\n")).upper()

            elif game_choice == "POKEMON CENTER":
                pc = Pokemon_Center(self.our_pokemon)
                
                game_choice = str(input("\nWhat would you like to do with {}?\n".format(self.our_pokemon.name)+
                "Please choose from the following game options:\n"+
                "['RENAME POKEMON', 'GET POKEMON STATS', 'PLAY', 'BATTLE', 'POKEMON CENTER', 'QUIT']\n")).upper()
        
        print("""\nThanks for playing POKEMON TRAINER!\n
            Your final Pokemon stats are: \n""")
        print(self.our_pokemon)
                           
                           
# ------------

game = GameTime()