from module import *

dict = {"А": "1", "Б": "2", "В": "3", "Г": "4", "Д": "5", "Е": "6", "Ё": "7", "Ж": "8", "З": "9", "И": "1", "Й": "2", "К": "3", "Л": "4", "М": "5", "Н": "6", "О": "7", "П": "8", "Р": "9", "С": "1", "Т": "2", "У": "3", "Ф": "4", "Х": "5", "Ц": "6", "Ч": "7", "Ш": "8", "Щ": "9", "Ъ": "1", "Ы": "2", "Ь": "3", "Э": "4", "Ю": "5", "Я": "6"}
letters_list = readDictKeys(dict)
numb_list = readDictVal(dict)

while True:
    try:
        name = input('Введите имя: ')
        verif = name.isalpha()

    except TypeError:
        print('Введите имя, состоящее из букв.')

    nameu = name.upper()
    getNameNumber(numb_list, letters_list, nameu)