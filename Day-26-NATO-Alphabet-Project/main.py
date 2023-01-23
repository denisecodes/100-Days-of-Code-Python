import pandas

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

check_word = True
while check_word:
    user_word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
    # Check through dictionary, if letter matches dictionary letter, add NATO alphabet to a list
    else:
        print(output_list)
        check_word = False
