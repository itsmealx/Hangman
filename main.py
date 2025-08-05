import random
import art
import words

word_to_guess = random.choice(words.word_list)

placeholder = "" #to give hint on how many letters there are to guess
for letter in range(len(word_to_guess)):
    placeholder += "_"
correct_letters = ""
game_over = False
player_lives = 6
total_lives = 6

print(art.logo)
print(f"Guess this {len(word_to_guess)} letter word: {placeholder}")
print(word_to_guess)

while not game_over:

    display = ""

    if player_lives == 1:
        print(f"Warning: You only have {player_lives} life remaining. Be sure to guess it right!")


    user_guess = input("Guess the letter: ").lower()

    #validation to check if input is valid and deduct one life for every wrong guess.
    if not user_guess.isalpha():
        print("Invalid input. Letters only.")
    elif len(user_guess) > 1:
        print("Only one letter is allowed.")
    elif user_guess not in word_to_guess:
        player_lives -= 1


    #check if letter is already guessed.
    if user_guess in correct_letters:
        print(f"You've already guessed the letter '{user_guess}'.")

    for letter in word_to_guess:
        if user_guess == letter:
            display += letter
            correct_letters += letter
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    if player_lives == 0:
        print("Uh oh. You have no more lives. Game over!")
        print(f"The right word is: {word_to_guess.upper()}")
        game_over = True
    else:
        print(f"Word to guess: {display}")
        print(f"Lives remaining: {player_lives}/{total_lives}")


    if "_" not in display:
        print(f"You've guess the word: {word_to_guess.upper()}.")
        print("Congratulations. You win!")
        game_over = True
    else:
        print(art.stages[player_lives])
