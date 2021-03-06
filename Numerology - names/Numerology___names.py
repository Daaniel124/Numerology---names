from module import *
import re

dictrus = {"А": "1", "Б": "2", "В": "3", "Г": "4", "Д": "5", "Е": "6", "Ё": "7", "Ж": "8", "З": "9", "И": "1", "Й": "2", "К": "3", "Л": "4", "М": "5", "Н": "6", "О": "7", "П": "8", "Р": "9", "С": "1", "Т": "2", "У": "3", "Ф": "4", "Х": "5", "Ц": "6", "Ч": "7", "Ш": "8", "Щ": "9", "Ъ": "1", "Ы": "2", "Ь": "3", "Э": "4", "Ю": "5", "Я": "6"}
dicteng = {"A": "1", "B": "2", "C": "3", "D": "4", "E": "5", "F": "6", "G": "7", "H": "8", "I": "9", "J": "1", "K": "2", "L": "3", "M": "4", "N": "5", "O": "6", "P": "7", "Q": "8", "R": "9", "S": "1", "T": "2", "U": "3", "V": "4", "W": "5", "X": "6", "Y": "7", "Z": "8"}
letters_eng = readDictKeys(dicteng)
numb_eng = readDictVal(dicteng)
letters_rus = readDictKeys(dictrus)
numb_rus = readDictVal(dictrus)

while True:
    try:
        name = str(input('Введите имя: '))
        verif = name.isalpha()
    except Exception:
        print('Введите имя, состоящее из букв.')

    if verif == True:
        nameu = name.upper()
        if re.search('[aA-zZ]', name):
            getNameNumber(numb_eng, letters_eng, nameu)
        elif re.search('[а-яА-ЯёЁ]', name):
            getNameNumber(numb_rus, letters_rus, nameu)
        else:
            print('Введите имя на русском или латинском')