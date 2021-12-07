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
