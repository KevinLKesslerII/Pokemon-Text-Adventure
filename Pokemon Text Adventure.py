import random

def battle(your_pokemon_name, opponent_name, opponent_hp):
    """Simulates a Pokémon battle.

    Args:
      your_pokemon_name: The name of your Pokémon.
      opponent_name: The name of the opponent Pokémon.
      opponent_hp: The initial HP of the opponent.
    """

    your_hp = 100
    
    while your_hp > 0 and opponent_hp > 0:
        print("\nYour", your_pokemon_name + "'s HP:", your_hp)
        print(opponent_name + "'s HP:", opponent_hp)

        action = input("What will you do? (attack/catch/run): ")

        if action == "attack":
            damage = random.randint(10, 20)
            opponent_hp -= damage
            print(your_pokemon_name, "attacks!", opponent_name, "takes", damage, "damage.")

            if opponent_hp <= 0:
                print("You defeated the wild", opponent_name + "!")
                return False  # Indicate that the Pokémon was not caught
            
            # Opponent's attack
            damage = random.randint(5, 15)
            your_hp -= damage
            print(opponent_name, "attacks!", your_pokemon_name, "takes", damage, "damage.")

        elif action == "catch":
            # Simple catch logic 
            catch_chance = random.randint(1, 10)
            if catch_chance > 4:  # 60% chance to catch
                print("You threw a Poké Ball... Gotcha!", opponent_name, "was caught!")
                return True  # Indicate that the Pokémon was caught
            else:
                print("You threw a Poké Ball... Oh no! The", opponent_name, "broke free!")

            # Opponent's attack after a failed catch attempt
            damage = random.randint(5, 15)
            your_hp -= damage
            print(opponent_name, "attacks!", your_pokemon_name, "takes", damage, "damage.")

        elif action == "run":
            print("You got away safely!")
            return False  # Indicate that the Pokémon was not caught
        else:
            print("Invalid action. Please choose 'attack', 'catch', or 'run'.")

    if your_hp <= 0:
        print(your_pokemon_name, "fainted! You blacked out...")
        return False  # Indicate that the Pokémon was not caught


# --- Main ---

print("Today is the day! Today you will be receiving your very first Pokemon from Professor Oak!\n")
print("You head to the Professor's Lab and greet him.\n")
print('Oak: "Why hello young one! Here for a Pokemon are you? Well that`s great! Before we proceed however, I need to know your name."\n')
name = input("What is your name?: ")
print('Oak: "So your name is', name, '? Splendid! Now let us get you situated with your very first Pokemon shall we?"\n')
print('Oak: "We have 3 choices for you: The fire type Charmander, the water type Squirtle, and the Grass type Bulbasaur."\n')


Pokemon_1 = input("Which do you choose? (This is case-sensitive): ")

pokemon_lower = Pokemon_1.lower()

if pokemon_lower == "bulbasaur":
    print('Oak: "The Grass type Bulbasaur eh? He is a great companion and is strong against Water, Rock, and Ground types!"\n')
elif pokemon_lower == "squirtle":
    print('Oak: "The Water type Squirtle eh? He is a very powerful and is strong against Fire, Rock, and Ground types!"\n')
else:
    print('Oak: "The Fire type Charmander eh? It burns down its opponents with its flames and is strong against Grass, Bug, Steel, and Ice types!!"\n')

print('Oak: "Now that you have your first Pokemon, you must journey to the all the different gyms, defeat the gym leaders, and challenge the Elite Four to become the strongest trainer in the region."\n')
print('Oak: "I wish you and ', Pokemon_1, 'the best of luck!!"')

print("\nNow that you have gotten your first Pokemon, your first stop is heading to the gym in Pewter City.")
print("To get there, you must pass through Route 1, Viridian City, Route 2, then to Viridian Forest.")

# --- Linear game progression ---

route = 1  # Start on Route 1
player_pokemon = [Pokemon_1]  # Initialize the list with the starter Pokémon

print("\nOn your way to Viridian City via Route 1, you encounter a wild Pokemon! Time to battle!")

possible_opponents = [("Pidgey", 80), ("Rattata", 70)]
opponent_name, opponent_hp = random.choice(possible_opponents)
print("A wild", opponent_name, "appears!")

if battle(Pokemon_1, opponent_name, opponent_hp):  # Check if the Pokémon was caught
    player_pokemon.append(opponent_name)  # Add caught Pokémon to the list
    Pokemon_2 = opponent_name  # Assign the caught Pokémon to Pokemon_2

print("After your battle with the", opponent_name, "you head to Route 2.\n")
print("Enjoying the trip, you decide to take a break with your Pokemon and enjoy the scenery.\n")
print("Before you can do so, a wild Pokemon appears!!\n")

# Route 2 encounter 
route = 2
possible_opponents = [("Caterpie", 60), ("Weedle", 60), ("Pidgey", 80), 
                      ("Rattata", 70), ("Nidoran(male)", 75), ("Nidoran(female)", 75)]
opponent_name, opponent_hp = random.choice(possible_opponents)
print("A wild", opponent_name, "appears!")

# Choose which Pokémon to use
print("\nYour Pokémon:")
for i, pokemon in enumerate(player_pokemon):
    print(f"{i+1}. {pokemon}")

choice = int(input("Which Pokémon do you want to use? ")) - 1  # Get player's choice (adjust for 0-indexing)
#battle(player_pokemon[choice], opponent_name, opponent_hp)

if battle(player_pokemon[choice], opponent_name, opponent_hp):  # Check if the Pokémon was caught
    player_pokemon.append(opponent_name)  # Add caught Pokémon to the list
    Pokemon_3 = opponent_name

print("\nAfter the encounter, you head into Viridian Forest.\n")
print("You get lost after wandering for 30 minutes, when suddenly, you are attacked by a wild Pokemon!\n")

route = "Viridian Forest"
possible_opponents = [("Caterpie", 60), ("Metapod", 70), ("Weedle", 60), 
                      ("Kakuna", 70), ("Pidgey", 80), ("Pidgeotto", 90), ("Pikachu", 100)]
opponent_name, opponent_hp = random.choice(possible_opponents)
print("A wild", opponent_name, "appears!")

# Choose which Pokémon to use
print("\nYour Pokémon:")
for i, pokemon in enumerate(player_pokemon):
    print(f"{i+1}. {pokemon}")

choice = int(input("Which Pokémon do you want to use? ")) - 1  # Get player's choice (adjust for 0-indexing)
#battle(player_pokemon[choice], opponent_name, opponent_hp)

if battle(player_pokemon[choice], opponent_name, opponent_hp):  # Check if the Pokémon was caught
    player_pokemon.append(opponent_name)  # Add caught Pokémon to the list
    Pokemon_4 = opponent_name

print("\nNow that you have made it through Viridian Forest, you have finally arrived in Pewter City.\n")
print("In Pewter City, the Gym Leader Brock awaits with his solid Rock Type Pokemon.\n")
decision = input("Would you like to head into the Gym or head back to the forest for more training? Select either Gym or Train: ")


if decision == "Gym":
    print("\nYou and your team steel yourselves and head into the Gym.")
else:
    print("\nYou feel unprepared for the challenge ahead, so you turn back and head into Viridian Forest for a little more training.")

print("\nThanks for playing this demo! This is still a WiP and will be updated regularly. Thanks and please look forward to the next part!")
    
