
class MorseCodeTranslator:
    
    def __init__(self):
        self.morse_code_dict = {
            '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',                                                #Die Dictionaries 'morse_code_dict' und 'textToMorsecode' haben wir von ChatGPT generieren lassen
            '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
            '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
            '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
            '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
            '--..': 'Z', '/': ' ',
            '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
            '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
            '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!',
            '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':',
            '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_',
            '.-..-.': '"', '...-..-': '$', '.--.-.': '@'
        }
        self.textToMorsecode = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
            'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
            'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    
            '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
            '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
            ' ': '/ ',
    
            '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
            '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.',
            '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
        }

        
    def morse_to_text(self, morse_code_in):                                    # Diese Funktion haben wir von ChatGPT
        words = morse_code_in.split(' / ')
        words = morse_code_in.split(' / ')
        decoded_message = ''
        for word in words:
            letters = word.split()
            for letter in letters:
                decoded_message += self.morse_code_dict.get(letter, '')
            decoded_message += ' '
        return decoded_message


class TextToMorseCodeTranslator(MorseCodeTranslator):

    def to_morse_code(self, text):
        morse_code = " ".join(self.textToMorsecode.get(c, '') for c in text.upper())
        return morse_code


class Program:
    
    def run():
        loop = True
        while loop:
            print("Willkommen zu unserem Morsecode Translator.")
            print("Wähle bitte aus, was du machen willst:")
            print("1) Text zu Morsecode übersetzen")
            print("2) Morsecode zu Text übersetzen")
            
            choice = input("Deine Wahl: ")

            if choice == '1':
                translator = TextToMorseCodeTranslator()
                text = input("Bitte gib einen Text ein: ")
                morse_code = translator.to_morse_code(text)
                print("Morsecode:", morse_code)

            elif choice == '2':
                translator = MorseCodeTranslator()
                morse_code = input("Bitte gib Morsecode ein: ")
                text = translator.morse_to_text(morse_code)
                print("Text:", text)

            else:
                print("Ungültige Eingabe.")

            option = input("Willst du nochmal übersetzen(1) oder das Programm beenden(2)? ")
            if option == '2':
                loop = False
            elif option != '1'and'2':
                print("ungültige Eingabe")


if __name__ == "__main__":
    Program.run()
