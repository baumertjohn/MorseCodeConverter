# Text to Morse Code Convertor
import os

# Create Dictionary of letters / code symbols
morse_code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
              'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
              'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
              'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
              'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
              'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
              '4': '....-', '5': '.....', '6': '-....', '7': '--...',
              '8': '---..', '9': '----.', '0': '-----'}


def main():
    # Clear screen and ask user for input
    os.system('cls')
    user_text = input("Enter text to convert to morse code.\n> ")

    # Parse input and add to string
    # Note non-alpha / non-num chars and spaces
    converted_text = ''
    for char in user_text.upper():
        if char.isalnum():
            converted_text += morse_code[char] + ' '
        elif char == ' ':
            converted_text += '/ '

    # Output converted text
    print(converted_text)


if __name__ == "__main__":
    main()
