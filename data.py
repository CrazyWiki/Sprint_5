import random
class FirstPersonData:
    first_person_user_name='Виктория Зелова'
    first_person_email='victoriazelova13889@ya.ru'
    first_person_password='123456'
class RandomiseData:
    first_names = ['Иван', 'Анастасия', 'Дмитрий', 'Екатерина', 'Сергей', 'Мария', 'Александр', 'Ольга']
    last_names = ['Иванов', 'Петров', 'Сидоров', 'Кузнецов', 'Смирнова', 'Попова', 'Васильева', 'Зайцева']
    random_person_user_name = f"{random.choice(first_names)} {random.choice(last_names)}"
    random_person_email = f"random_person_user_name{random.randint(10000, 99999)}"
    random_person_password = random.randint(100000, 9999999)