import os

# Globální konstanty a proměnné
MY_ALPHABET = "aábcčdďeéěfghijklmnňoópqrřsštťuůúvwxyzž0123456789.,-+?!AÁBCČDĎEÉĚFGHIJKLMNŇOÓPQRŘSŠTŤUŮÚVWXYZŽ"
# Definujeme české znaky a jejich pořadí, protože v ASCII tabulce nejsou po sobě

SECRET_TEXT = "Vo 80 +trtx 8ňw0+o óňzrň ó04p, 6ú y.6í 204ňrú8 6s +7íy Pňs6ň40+ú ůňyóň"
# Caesarův tajný text pro odšifrování


def caesar_cipher_decrypt(encrypted_text: str, shift: int, alphabet: str) -> str:
    """
    Decrypts a Caesar cipher by shifting each character in the text.

    :param encrypted_text: The text to decrypt.
    :param shift: The number of positions to shift each character in the alphabet.
    :param alphabet: The alphabet to use for the decryption.
    :return: The decrypted text.
    """
    text = ""
    alphabet = list(alphabet)

    for char in encrypted_text:
        if char == " ":
            text += " "
            continue

        try:
            index_to_add = alphabet.index(char) - shift
        except ValueError:
            text += char
            continue

        if index_to_add < 0:
            index_to_add += len(alphabet)

        text += alphabet[index_to_add % len(alphabet)]

    return text


def caesar_cipher_multi_shift(text: str, shifts: list) -> str:
    """
    Encrypts text using a Caesar cipher with multiple shifts for each character.

    :param text: The text to encrypt.
    :param shifts: A list of shifts to apply to each character, cycling through the list.
    :return: The encrypted text.
    """
    alphabet = list(MY_ALPHABET)
    encrypted_text = ""

    for i, char in enumerate(text):
        if char == " ":
            encrypted_text += " "
            continue

        index_to_add = alphabet.index(char) + shifts[i % len(shifts)]

        if index_to_add > len(alphabet) - 1:
            index_to_add -= len(alphabet)

        encrypted_text += alphabet[index_to_add % len(alphabet)]

    return encrypted_text


def caesar_cipher_multi_shift_decrypt(encrypted_text: str, shifts: list) -> str:
    """
    Decrypts a Caesar cipher with multiple shifts applied to each character.

    :param encrypted_text: The text to decrypt.
    :param shifts: A list of shifts used in the encryption, cycling through the list.
    :return: The decrypted text.
    """
    text = ""
    alphabet = list(MY_ALPHABET)

    for i, char in enumerate(encrypted_text):
        if char == " ":
            text += " "
            continue

        index_to_add = alphabet.index(char) - shifts[i % len(shifts)]

        if index_to_add < 0:
            index_to_add += len(alphabet)

        text += alphabet[index_to_add % len(alphabet)]

    return text


def caesar_word_shift(text: str, shift: int) -> str:
    """
    Shifts words in a sentence based on a given shift value.

    :param text: The sentence to shift.
    :param shift: The number of positions to shift each word in the sentence.
    :return: The sentence with words shifted.
    """
    splitted_words = text.split()
    encrypted_text = ""

    for word in splitted_words:
        i = splitted_words.index(word) + shift

        if i > len(splitted_words) - 1:
            i -= len(splitted_words)
        elif i < 0:
            i += len(splitted_words)

        encrypted_text += " " + splitted_words[i]

    return encrypted_text


if __name__ == "__main__":
    os.system("clear")

    # Caesar s posunem každého znaku o jiný počet dle šablony
    print("Caesarova šifra s různým posunem znaků\n")
    input_text = input("Zadejte text, ideálně větu nebo souvětí pro zašifrování: ")

    shifts = [1, 5, 13, 19, 8]  # Cyklus posunů
    print("Vzor pro posun: ", shifts)

    encrypted_text = caesar_cipher_multi_shift(input_text, shifts)
    print("Zašifrovaný text:", encrypted_text)

    decrypted_text = caesar_cipher_multi_shift_decrypt(encrypted_text, shifts)
    print("Odšifrovaný text:", decrypted_text)
    print("------------------------------------------------\n")

    # Caesar test s posunem celých slov - v1
    print("Caesarova šifra s posunem slov - v1\n")
    shift = int(input("Zadejte číslo pro posun slov v původní větě: "))

    encrypted_text = caesar_word_shift(input_text, shift)
    print("Zašifrovaná věta:", encrypted_text)

    decrypted_text = caesar_word_shift(encrypted_text, -shift)
    print("Odšifrovaná věta:", decrypted_text)
    print("------------------------------------------------\n")

    # Caesarova tajenka - vzkaz, Vzkoušíme všechny možné posuny a vypíšeme výsledky, manuálně hledáme smysluplnou větu
    print("Caesar hrubou silou\n")
    print(f"Zašifrovaná věta: {SECRET_TEXT}\n")

    for i in range(1, len(SECRET_TEXT)):
        print(f"{i}. pokus: {caesar_cipher_decrypt(SECRET_TEXT, i, MY_ALPHABET)}")