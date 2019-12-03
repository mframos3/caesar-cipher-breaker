import math

# Frequencies for letters in the alphabet from A to Z.
ENGLISH_FREQUENCIES = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228,
                       0.02015, 0.06094, 0.06966, 0.00153, 0.00772, 0.04025,
                       0.02406, 0.06749, 0.07507, 0.01929, 0.00095, 0.05987,
                       0.06327, 0.09056, 0.02758, 0.00978, 0.02360, 0.00150,
                       0.01974, 0.00074]


def get_character_entropy(character):
    if character.isupper():
        return math.log(ENGLISH_FREQUENCIES[ord(character) - 65])
    elif character.islower():
        return math.log(ENGLISH_FREQUENCIES[ord(character) - 97])
    return


def alphabet_characters_entropy_sum(string):
    return sum([get_character_entropy(character)
               for character in string
               if character.isalpha()])


def non_alphabet_characters_count(string):
    return len([character for character in string
                if not character.isalpha()])


def string_entropy(string):
    return - alphabet_characters_entropy_sum(string) / math.log(2) / \
        (len(string) - non_alphabet_characters_count(string))


def mod(x, y):
    return (x % y + y) % y


def shift_character(character, key):
    if character.isupper():
        return chr(mod(ord(character) - 65 - key, 26) + 65)
    elif character.islower():
        return chr(mod(ord(character) - 97 - key, 26) + 97)
    else:
        return character


def decrypt(string, key):
    return "".join([shift_character(character, key) for character in string])


def get_all_shifts_data(string):
    return [{"string": decrypt(string, i),
             "key": i,
             "entropy": string_entropy(decrypt(string, i))}
            for i in range(0, 26)]


def remove_original_string(shifts, string):
    return list(filter(lambda shift: shift["string"] != string, shifts))


def decipher(string):
    shifts_sorted_by_entropy = sorted(get_all_shifts_data(string),
                                      key=lambda shift: shift["entropy"])
    best_guess = remove_original_string(shifts_sorted_by_entropy, string)[0]
    print_results(best_guess, shifts_sorted_by_entropy)


def print_results(best_guess, shifts):
    print(f"BEST GUESS: {best_guess['string']}\n")
    print("all guesses ordered by entropy:\n")
    for item in shifts:
        print(f"guess: {item['string']}, "
              f"key: {item['key']}, "
              f"entropy: {item['entropy']}")


decipher(input("Insert string to decipher\n"))
