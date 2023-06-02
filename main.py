from art import logo, vs
from game_data import data
import random
import os

def clear():
    """Clears the terminal screen."""
    os.system('clear')

def print_player(player):
    """Prints the details of a player."""
    name = player['name']
    description = player['description']
    country = player['country']
    followers = player['follower_count']
    print(f"{name}, a {description}, from {country}")

def compare_followers(player1, player2):
    """Compares the number of followers between two players and returns 'a' if player1 has more followers, 
    'b' if player2 has more followers, or None if they have the same number of followers."""
    followers1 = player1['follower_count']
    followers2 = player2['follower_count']
    if followers1 > followers2:
        return "a"
    elif followers1 < followers2:
        return "b"
    else:
        return None

def play_game():
    """Plays the game."""
    score = 0
    should_continue = True
    player1 = random.choice(data)

    while should_continue:
        player2 = random.choice(data)
        while player2 == player1:
            player2 = random.choice(data)

        # Display the game interface
        print(logo)
        print(f"Compare A:")
        print_player(player1)
        print(vs)
        print(f"Against B:")
        print_player(player2)

        # Prompt the user for their guess
        guess = input("Who has more followers? 'A' or 'B': ").lower()

        clear()

        if guess == compare_followers(player1, player2):
            # If the guess is correct, increase the score and continue to the next round
            score += 1
            print(f"You are right! Current score: {score}")
            player1 = player2
        else:
            # If the guess is incorrect, end the game and display the final score
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            should_continue = False

play_game()
