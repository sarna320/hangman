import random
import hangman_stages

word_list = ["aardvark", "baboon", "camel"]

# chosen_word=word_list[random.randint(0,len(word_list)-1)]
chosen_word = random.choice(word_list)
display = ["_"] * len(chosen_word)
lives=6
while "_" in display and lives>0:
    guess = input("Guess a letter: ").lower()
    was_found=False

    for i in range(0, len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
            was_found=True
    if(was_found==False):
        lives-=1
    print(f"{' '.join(display)}")
    print(hangman_stages.stages[lives])
if(lives>0):
    print("You win")
else:
    print("You lose")