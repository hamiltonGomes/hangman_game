import time

from create_secrets_words import create_secrets_words_in_file


class HangmanGame:

    def __init__(self, username=None):
        self.__username = username

    def play_game(self):
        secret_word_generator = self.generate_secret_word()
        secret_word = next(secret_word_generator).lower()

        attempts = 0
        loser = False
        winner = False

        self.welcome()
        time.sleep(1)

        correct_letters = self.word_print(secret_word)
        # print(secret_word)
        print(f"{correct_letters}\n")

        while not loser and not winner:
            guess = self.ask_for_guess()

            if guess in secret_word:
                self.correct_guess(secret_word, guess, correct_letters)
            else:
                attempts += 1
                self.wrong_guess(attempts)

            loser = attempts == 7
            winner = " _ " not in correct_letters

            print(f"{correct_letters}\n")

        time.sleep(1)
        if winner:
            self.winner_print()
        else:
            self.loser_print()

    def welcome(self):
        print("*" * 29)
        print("* Welcome to Hangman Game! *")
        print("*" * 29)
        time.sleep(1)
        print("\nI hope you enjoy my game and have some fun!")
        self.__username = input("But first, tell me your name:\n")
        print(f"\nLet's start, {self.__username}!")
        print("The theme of the game is people's names.\n")

    def generate_secret_word(self):
        create_secrets_words_in_file()
        with open("secrets_words.txt", "r") as file:
            secrets_words_list = file.read().split("\n")
            for word in secrets_words_list:
                yield word

    def word_print(self, secret_word):
        return [" _ " for letter in secret_word]

    def ask_for_guess(self):
        guess = input("What's your guess?\n").strip().lower()[0]
        return guess

    def correct_guess(self, secret_word, guess, correct_letters):
        index = 0
        for letter in secret_word:
            if guess == letter:
                correct_letters[index] = letter
            index += 1

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
        time.sleep(1)
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
    hangman_game = HangmanGame()
    hangman_game.play_game()
