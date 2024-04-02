class MorseMsg:
    eng_morse = {'-.': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '–.': 'G', '....': 'H',
                 '..': 'I', '.—': 'J', '-.-': 'K', '.-..': 'L', '–': 'M', '-.': 'N', '—': 'O', '.–.': 'P',
                 '–.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V',
                 '.–': 'W', '-..-': 'X', '-.–': 'Y', '–..': 'Z'}
    rus_morse = {'.-': 'А', '-...': 'Б', '.–': 'В', '–.': 'Г', '-..': 'Д', '.': 'Е',
                 '...-': 'Ж', '–..': 'З', '..': 'И', '.—': 'Й', '-.-': 'К', '.-..': 'Л',
                 '–': 'М', '-.': 'Н', '—': 'О', '.–.': 'П', '.-.': 'Р', '...': 'С',
                 '-': 'Т', '..-': 'У', '..-.': 'Ф', '....': 'Х', '-.-.': 'Ц',
                 '—.': 'Ч', '—-': 'Ш', '–.-': 'Щ', '.–.-.': 'Ъ', '-..-': 'Ь',
                 '..-..': 'Э', '..–': 'Ю', '.-.-': 'Я'}

    def __init__(self, code):
        self.code = code

    def eng_decode(self):
        """
        Method that translates from Morse into English
        """
        eng_morse_list = self.code.split()
        eng_letter = ''.join([MorseMsg.eng_morse[eng_morse_list[i]] for i in range(len(eng_morse_list))])
        return eng_letter

    def ru_decode(self):
        """
        Method that translates from Morse into Russian
        """
        ru_morse_list = self.code.split()
        ru_letter = ''.join([MorseMsg.rus_morse[ru_morse_list[i]] for i in range(len(ru_morse_list))])
        return ru_letter

    def get_vowels(self, lang):
        """
        Method that outputs only vowels
        """
        if lang == 'ru':
            letters = ['Ё', 'У', 'Е', 'Ы', 'А', 'О', 'Э', 'Я', 'И', 'Ю']
            letters_ru = list(self.ru_decode())
            vowels = [letters_ru[i] for i in range(len(letters_ru)) if letters_ru[i] in letters]
            return vowels
        if lang == 'eng':
            letters = ['A', 'E', 'I', 'U', 'O']
            letters_eng = list(self.eng_decode())
            vowels = [letters_eng[i] for i in range(len(letters_eng)) if letters_eng[i] in letters]
            return vowels

    def get_consonants(self, lang):
        """
        Method that outputs only consonants
        """
        if lang == 'ru':
            letters = ['Ё', 'У', 'Е', 'Ы', 'А', 'О', 'Э', 'Я', 'И', 'Ю']
            letters_ru = list(self.ru_decode())
            consonants = [letters_ru[i] for i in range(len(letters_ru)) if letters_ru[i] not in letters]
            return consonants
        if lang == 'eng':
            letters = ['A', 'E', 'I', 'U', 'O']
            letters_eng = list(self.eng_decode())
            consonants = [letters_eng[i] for i in range(len(letters_eng)) if letters_eng[i] not in letters]
            return consonants

morse_msg = MorseMsg('..- –.. -.-.')
print(morse_msg.eng_decode())
print(morse_msg.ru_decode())
print(morse_msg.get_vowels('eng'))
print(morse_msg.get_vowels('ru'))
print(morse_msg.get_consonants('eng'))
print(morse_msg.get_consonants('ru'))