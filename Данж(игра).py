#--------------------------------------------------
# Автор: Иван Макидон (DR_makentoshi)
# Версия: 0.0.1
#--------------------------------------------------
import random 

score = 0
# Переменные - характеристики героя и противников
hero_class = ''
health_of_hero = 0
health_of_enemy = 0
attack_hero = 0
attack_enemy = 0
# Переменные ниже - противники,
enemy_low = ['зомби', 'гоблин']     # слабые противники
enemy_middle = ['колдун', 'вампир'] # средние противники 
enemy_high = ['виверна', 'призрак'] # сильные портивники
boss = 'Мясник'                     # Финальный босс
# конец переменных-противников
phaze_enemy = ''                  # выбранный противник в фазе

print("Ты очень смелый, если решился бросить вызов демонической крепости.\n\
Войди во врата и прими бой с смертельно опасными монстрами...\n\n\
Цель игры: набрать как можно больше очков\n\
Если готов, нажми \"Enter\"")
# Начало игры
input()

# Выбор класса
print("выбери класс своего героя(набери цифру напротив):\nВойн - 1\nМаг - 2\n\
Титан - 3\nПроклятый - 4")

# Начало описания классов
print("\nПройдемся немного по особенностям представленных тебе классов.\n\
Войн - если тебе не хочется особо много думать головой в процессе игры, то \
можешь выбрать этот класс. Идеально подходит для новичков\n\
(Добавляет +4 очка к общему счету)\n")
print("Маг - очень ловкий и коварный. Он владеет магическими заклинаниями, \
которые помогут тебе в борьбе с противником\n\
(Добавляет +2 очка к общему счету, Позволяет использовать способность \
замораживать противника и увеличивать урон, но лишь на одну фазу боя)\n")
print("Титан - порожденное великой рассой Титанов существо. \
Очень силен и вынослив, но не имеет возможности подбирать полезные предметы\n\
(Добавляет +2 очка к общему счету)\n")
print("Проклятый - прислужник нежити\n(Нет полезных свойств)")
# конец описания классов

print("Твой выбор: ")
hero_class = input()
if hero_class == '1':
    print("Ты выбрал Война")
    health_of_hero = 130
    attack_hero = 80
    print("Твое здоровье:", health_of_hero ,"HP\n",
          "Твоя атака:", attack_hero ,"POINTS")
    score = 4
elif hero_class == '2':
    print("Ты выбрал Мага")
    health_of_hero = 90
    attack_hero = 70
    print("Твое здоровье:", health_of_hero ,"HP\n",
          "Твоя атака:", attack_hero ,"POINTS")
    score = 2
elif hero_class == '3':
    print("Ты выбрал Титана")
    health_of_hero = 140
    attack_hero = 100
    print("Твое здоровье:", health_of_hero ,"HP\n",
          "Твоя атака:", attack_hero ,"POINTS")
    score = 2
elif hero_class == '4':
    print("Ты выбрал Проклятого")
    health_of_hero = 100
    attack_hero = 75
    print("Твое здоровье:", health_of_hero ,"HP\n",
          "Твоя атака:", attack_hero ,"POINTS")
else:
    print("Код твоего класса неверен. Перезайди в игру!!!")
    exit()

hero_class = int(hero_class)

print("------------------1 УРОВЕНЬ------------------")
input("Продолжить")
# Самый главный цикл - это комната на одном уровне.
# Всего может быть 3 комнаты в каждой по 10 фаз боя(второй цикл).
# Последний уровень - битва с боссом

# 1 комната 
for phaze in range(10):
    phaze_enemy = random.choice(enemy_low)

    print("На тебя нападает -",phaze_enemy)
    if phaze_enemy == 'зомби':
        health_of_enemy = 60
        attack_enemy = 30
    elif phaze_enemy == 'гоблин':
        health_of_enemy = 75
        attack_enemy = 45

    while health_of_enemy > 0 or health_of_hero > 0:
        first_move = random.randint(0,1)
        if first_move == 0:
            input("Ход противника")
            health_of_hero = health_of_hero - attack_enemy
            print("Твое здоровье",health_of_hero)
        if first_move == 1:
            input("Твой ход")
            health_of_enemy = health_of_enemy - attack_hero
            print("Здоровье противника",health_of_enemy)
        if health_of_enemy < 0:
            print("Противник мертв")
            break
        elif health_of_hero < 0:
            print("Ты погиб")
            exit()
input("Press \"Enter\" for exit ")
