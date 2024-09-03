import random
class FirstPersonData:
    first_person_user_name='Виктория Зелова'
    first_person_email='victoriazelova13889@ya.ru'
    first_person_password='123456'


def transliterate(name):
    slovar = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo',
              'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
              'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h',
              'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e',
              'ю': 'u', 'я': 'ya', 'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'YO',
              'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N',
              'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H',
              'Ц': 'C', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SCH', 'Ъ': '', 'Ы': 'y', 'Ь': '', 'Э': 'E',
              'Ю': 'U', 'Я': 'YA'}


    for key in slovar:
        name = name.replace(key, slovar[key])
    return name


class RandomiseData:
    first_names = ['Иван', 'Анастасия', 'Дмитрий', 'Екатерина', 'Сергей', 'Мария', 'Александр', 'Ольга']
    last_names = ['Иванов', 'Петров', 'Сидоров', 'Кузнецов', 'Смирнова', 'Попова', 'Васильева', 'Зайцева']
    random_person_user_name= f"{random.choice(first_names)}"
    random_person_user_last_name = f"{random.choice(last_names)}"
    random_person_user_full_name = f"{random_person_user_name} {random_person_user_last_name}"
    random_person_email = f"{transliterate(random_person_user_name)}{transliterate(random_person_user_last_name)}{random.randint(10000, 99999)}{'@yandex.ru'}"
    random_person_password = random.randint(100000, 9999999)
