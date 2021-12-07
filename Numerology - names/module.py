def readDictVal(dic: dict)->list:
    """
    Читает значения из словаря и добавляем их в список
    :param dict dic: Название словаря
    """
    mas = []
    for v in dic.values():
        mas.append(v.strip(''))
    return mas

def readDictKeys(dic: dict)->list:
    """
    Читаем ключи из словаря и добавляем их в список
    :param dict dic: Название словаря
    """
    mas = []
    for v in dic.keys():
        mas.append(v.strip(''))
    return mas

def getNameNumber(dictionary, name:str):
    """
    """
    name_list = list(name)
    print(name_list)
    name_numbers = 0

    for i in name_list:
        name_numbers += dictionary.get(i)
        
    print(name_numbers)
