from game_interface import *

hangman_game = GameLogic()
secret_word_generator = hangman_game.generate_secret_word()
secret_word = next(secret_word_generator)
print(secret_word)

# hangman_game.welcome()
# attempts = hangman_game.choose_level()

hangman_game.word_print(secret_word)
