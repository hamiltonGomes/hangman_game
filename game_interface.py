import time


class GameLogic:

    def __init__(self, username=None):
        self.__username = username

    def play_game(self):
        secret_word_generator = self.generate_secret_word()
        secret_word = next(secret_word_generator).lower()
        attempts = 0
        hanged = False

        self.welcome()
        self.word_print(secret_word)

        print(secret_word)

        while not hanged:
            guess = self.ask_for_guess()
            attempts += 1

            if guess in secret_word:
                # correct_guess()
                print("oi")
            else:
                self.wrong_guess(attempts)
            if attempts == 7:
                hanged = True

        # while not hanged and

    def welcome(self):
        print("*" * 29)
        print("* Welcome to Hangman Game! *")
        print("*" * 29)
        time.sleep(1)
        print("\nI hope you enjoy my game and have some fun!")
        self.__username = input("But first, tell me your name:\n")
        print(f"\nLet's start, {self.__username}!")
        print("The theme of the game is people's names.")

    def generate_secret_word(self):
        with open("secrets_words.txt", "r") as file:
            secrets_words_list = file.read().split("\n")
            for word in secrets_words_list:
                yield word

    def word_print(self, secret_word):
        print([" _ " for letter in secret_word])

    def ask_for_guess(self):
        guess = input("What's your guess?").strip().lower()
        return guess

    # def choose_level(self):
    #     level = 0
    #
    #     while level not in [1, 2, 3, 4]:
    #         time.sleep(1)
    #         print()
    #         print("*" * 14)
    #         print("* DIFFICULTY *")
    #         print("*" * 14)
    #         print("1. Easy")
    #         print("2. Normal")
    #         print("3. Hard")
    #         print("4. Hardcore")
    #         level = int(input("What level do you want to try?"))
    #
    #     if level == 1:
    #         attempts = 10
    #     elif level == 2:
    #         attempts = 5
    #     elif level == 3:
    #         attempts = 3
    #     elif level == 4:
    #         attempts = 1
    #
    #     return attempts

    # def correct_guess(self):

    def wrong_guess(self, attempts):
        print("  _______     ")
        print(" |/      |    ")

        if attempts == 1:
            print(" |      (_)   ")
            print(" |            ")
            print(" |            ")
            print(" |            ")

        if attempts == 2:
            print(" |      (_)   ")
            print(" |      \     ")
            print(" |            ")
            print(" |            ")

        if attempts == 3:
            print(" |      (_)   ")
            print(" |      \|    ")
            print(" |            ")
            print(" |            ")

        if attempts == 4:
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |            ")
            print(" |            ")

        if attempts == 5:
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |            ")

        if attempts == 6:
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      /     ")

        if attempts == 7:
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      / \   ")

        print(" |            ")
        print("_|___         ")
        print()

    def winner_print(self):
        print(f"Congratulations, {self.__username}! You win!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")

    def loser_print(self):
        print("Oh, good try, but you died.")
        time.sleep(1)
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")
        print(f"Try again, {self.__username}! Don't give up!")
        print(f"The secret word was {self.__username}.")


if __name__ == '__main__':
    hangman_game = GameLogic()
    hangman_game.play_game()
