import random
from hangman_guessing import guess_list
from hangman_life import game_name, lives

print(game_name)
guessing_word=random.choice(guess_list).lower()
word_letters=len(guessing_word)
game_over=False
tries=6
result=[]
for _ in range(word_letters):
    result+='_'
while not game_over:
    user_guessing=input('Guess a letter: ')
    if user_guessing in result:
        print(f'The letter you have guessed is: {user_guessing}')
    for pos in range(word_letters):
        letter=guessing_word[pos]
        if letter==user_guessing:
            result[pos]=letter
    if user_guessing not in guessing_word:
        print(f'You guessed {user_guessing}. One try lost!!')
        tries-=1
        if tries==0:
            game_over=True
            print(f'The word supposed to be guessed is: {guessing_word}')
            print('Game over!!')
    print(f"{' '.join(result)}")
    if '_' not in result:
        game_over=True
        print(f'The word you guessed is: {guessing_word}')
        print('You win!!')
    print(lives[tries])