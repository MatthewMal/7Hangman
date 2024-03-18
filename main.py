import random
from game_data import logo, stages, word_list

goal = random.choice(word_list)
string_list = ["_"] * len(goal)

mistakes = 0
end_of_game = False
guessed = []
print(logo)
while mistakes < 6 and not end_of_game:
    guess = (input("Enter a letter:")).lower()
    if guess in guessed:
        print(f"\nYou already guessed letter {guess}\n")
        print(stages[mistakes])
        print("".join(string_list) + "\n")
    else:
        if guess in goal:
            for i in range(len(string_list)):
                if goal[i] == guess:
                    string_list[i] = guess
        else:
            mistakes += 1
            print(f"\n{guess} is not a match")
        print(stages[mistakes])
        print("".join(string_list) + "\n")
        guessed.append(guess)
    if "_" not in string_list:
        end_of_game = True
if mistakes < 6:
    print("Congratulations, you won!")
else:
    print("You lost")
    print(f"The word was {goal}")
