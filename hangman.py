import random

actors_list = [
    {"name": "Leonardo DiCaprio", "hint": "Famous for his role in Titanic"},
    {"name": "Meryl Streep", "hint": "One of the most acclaimed actresses in Hollywood"},
    {"name": "Brad Pitt", "hint": "Known for his roles in Fight Club and Inglourious Basterds"},
    {"name": "Julia Roberts", "hint": "Starred in Pretty Woman and Erin Brockovich"},
    {"name": "Tom Hanks", "hint": "Known for Forrest Gump and Cast Away"}
]

lives = 6

def choose_actor(actors_list):
    return random.choice(actors_list)

def display_actor(actor, guessed_letters):
    display = ""
    for char in actor["name"]:
        if char.lower() in guessed_letters or char == " ":
            display += char
        else:
            display += "_"
    return display

chosen_actor = choose_actor(actors_list)
guessed_letters = []

print("Welcome to Hangman - Actors' Names Edition!")

game_over = False

while not game_over:

    print(f"Lives left: {lives}")
    print(display_actor(chosen_actor, guessed_letters))
    print("Hint:", chosen_actor["hint"])

    user_guess = input("Guess a letter: ").lower()

    if user_guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(user_guess)

    if user_guess not in chosen_actor["name"].lower():
        lives -= 1
        if lives == 0:
            game_over = True
            print(f"You Lose! The actor's name was '{chosen_actor['name']}'.")
    else:
        if "_" not in display_actor(chosen_actor, guessed_letters):
            game_over = True
            print(f"Congratulations! You Win! The actor's name was '{chosen_actor['name']}'.")

print("Thank you for playing Hangman - Actors' Names Edition!")
