import random
import os
import pyglet
import time


def finish_calculation_result(win_hum, win_com):
    """
    Итоговый подсчет очков
    :param win_hum: кол-во побед человека
    :param win_com: кол-во побед компьютера
    :return: результат
    """

    win_people = ['Победитель по жизни', 'Чуствуешь? Это сладкий запах победы',
                  'Вы получили ачивку: "Победитель Скайнета"']
    lose_people = ['Как всегда, проиграл', 'Что с лицом, кожанный? ', 'Проиграл какой-то железяки']
    draw = ['Такое вообще бывает? НИЧЬЯ', 'Объявляю вас мужем и женой',
            'Вам будет о чем поговорить']

    print(f'\n\tРезультат. Барабанная дробь')
    song = pyglet.media.load('baraban.mp3')
    song.play()
    time.sleep(5)

    if win_hum == win_com:
        print(f'\n\t{random.choice(draw)}\n')
        time.sleep(5)
        os.system('cls||clear')
        return 'no_win'

    elif win_hum > win_com:
        print(f'\n\t{random.choice(win_people)}\n')
        time.sleep(5)
        os.system('cls||clear')
        return 'hum'
    else:
        print(f'\n\t{random.choice(lose_people)}\n')
        time.sleep(5)
        os.system('cls||clear')
        return 'com'


def calculation_round_result(choosing_human, choosing_computer):
    """
    Подсчет результата раунда
    :param choosing_human: кол-во побед человека
    :param choosing_computer:  кол-во побед компьюрета
    :return: результат
    """

    win_people = ['Вы взяли раунд', 'КрасаВчик', 'Идешь к успеху']
    lose_people = ['Кожанный мешок', 'В следующий раз повезет', 'Постарайся(']
    draw = ['Гении думают одинакого', 'У вас есть много общего', 'Чудесааа. Ничья.....']

    if choosing_human == choosing_computer:
        print(f'\t{random.choice(draw)}')
        return 'no_win'

    elif choosing_human == "Камень":
        if choosing_computer == "Ножницы":
            print(f'\t{random.choice(win_people)}')
            return 'hum'
        else:
            print(f'\t{random.choice(lose_people)}\n')
            return 'com'

    elif choosing_human == "Ножницы":
        if choosing_computer == "Бумага":
            print(f'\t{random.choice(win_people)}\n')
            return 'hum'
        else:
            print(f'\t{random.choice(lose_people)}\n')
            return 'com'

    else:
        if choosing_computer == "Камень":
            print(f'\t{random.choice(win_people)}\n')
            return 'hum'
        else:
            print(f'\t{random.choice(lose_people)}\n')
            return 'com'


def play_game():
    """
    Исполнение основной игры
    :return: итоговый результат игры
    """

    win_com, win_hum = 0, 0
    game_elements = ["Камень", "Ножницы", "Бумага"]

    os.system('cls||clear')
    print("\t******* Игра начинается *******\n")

    remember_the_rules = input("\tНапомнить правила игры? Да/Нет: ")

    if remember_the_rules.strip() == 'Да':
        print('\tИгрок и компьютер выбирают один из трех знаков: Камень, Ножницы или Бумага\n'
              '\tПосле выборов идет определение победителя\n'
              '\tПобедитель определяется по следующим правилам:\n'
              '\t\t* Бумага побеждает камень («бумага обёртывает камень»).\n'
              '\t\t* Камень побеждает ножницы («камень затупляет или ломает ножницы»).\n'
              '\t\t* Ножницы побеждают бумагу («ножницы разрезают бумагу»).\n'
              '\tЕсли игроки показали одинаковый знак, то засчитывается ничья\n'
              '\tИгра состоит из 3 раундов\n\n')

    round_game = 1

    while round_game <= 3:
        print(f'\n\t******* Раунд {round_game} *******')
        choosing_computer = random.choice(game_elements)
        choosing_human = ''

        print('\tКомпьютер сделал выбор.')
        while choosing_human.strip() not in game_elements:
            print('\tТеперь ваш выбор: ("Камень","Ножницы","Бумага")')
            choosing_human = input("\t")

        round_result = calculation_round_result(choosing_human, choosing_computer)

        if round_result == 'hum':
            win_hum += 1
        elif round_result == 'com':
            win_com += 1

        round_game += 1

    return finish_calculation_result(win_hum, win_com)


def statistics(score_game, name_hum):
    """
    Вывод статистики
    :param score_game: очки игроков
    :param name_hum:  имя пользователя
    """

    statis_word = ['Таки что тут у нас: ', 'Статистика такова: ', 'Будем посмотреть: ']
    win_people = ['Не теряй планку', 'Ты просто как машина. Хотя НЕТ. Даже лучше', 'Круче тебя только вареные яйца']
    lose_people = ['Наверное не твой день', 'Не повезло в игре - повезет в любви\n\t...........\n\tХотяяяяяя....',
                   'Все еще можно исправить']
    draw = ['Интереснинькооо', 'Таки шо так? Исправить ', f'Поднажми, {name_hum}']

    os.system('cls||clear')
    print(f'\n\t{random.choice(statis_word)}\n '
          f'\n\t\t* {name_hum}: {score_game["hum"]}'
          f'\n\t\t* Компьютер: {score_game["com"]}\n'
          )

    if score_game['hum'] > score_game['com']:
        print(f"\t{random.choice(win_people)}")
    elif score_game['hum'] < score_game['com']:
        print(f"\t{random.choice(lose_people)}")
    else:
        print(f"\t{random.choice(draw)}")

    time.sleep(3)
    os.system('cls||clear')


def main_menu():
    #Главное меню приложения

    player_choice = 0
    score_game = {
        "hum": 0,
        "com": 0,
        "no_win": 0
    }

    print("\t******* Добро пожаловать в игру 'Камень, ножницы, бумага' *******\n")

    name_hum = input("\tВведите Ваше имя: ")

    print(f"\n\tПриветствую, {name_hum}.")

    while player_choice != '3':
        print("\tВыберите команду из меню: ")
        print("\t1) Начать игру\n"
              "\t2) Посмотреть статистику\n"
              "\t3) Выход")

        player_choice = input("\tВаш выбор: ").strip()

        match player_choice:
            case '1':
                result = play_game()
                score_game[result] = score_game[result] + 1
            case '2':
                statistics(score_game, name_hum)
            case '3':
                continue
            case _:
                print('\n\tВсе фигня! Давай по-новой')
                continue

        print(f"\n\tЧто будем делать дальше, {name_hum}?")


if __name__ == '__main__':
    os.system('cls||clear')
    main_menu()
    os.system('cls||clear')
