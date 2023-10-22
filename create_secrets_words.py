from faker import Faker
from unidecode import unidecode

fake = Faker('pt_BR')


def create_secrets_words_in_file():
    secret_words_list = []
    for _ in range(0, 101):
        secret_word = fake.name()
        secret_word = secret_word.split()
        if any(term in secret_word for term in ['Dra.', 'Dr.', 'Sr.', 'Sra.', 'Srt.', 'Srta.']):
            secret_word = secret_word[1]
        else:
            secret_word = secret_word[0]
        secret_words_list.append(secret_word)

    with open("secrets_words.txt", "w") as file:
        for word in secret_words_list:
            file.write(unidecode(word) + "\n")
