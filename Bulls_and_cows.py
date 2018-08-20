import random

# создаём список всех возможных ответов
def get_all_answers():
    ans = []
    for i in range(10000):
        tmp = str(i).zfill(4)
        # Вариант 1 - множества
        if len(set(map(int, tmp))) == 4:
            ans.append(list(map(int, tmp)))
        # Вариант 2 - генератор списков
        lst = ['x' for num in tmp if tmp.count(num) ==1]
        if len(lst) == 4:
            ans.append(list(map(int, tmp)))
    return ans


# Выбираем один ответ из списка возможных
def get_one_answer(ans):
    num = random.choice(ans)
    return num


# Валидация ввода - четыре не повторяющиеся цифры
def input_number():
    while True:
        nums = input('Введите 4 неповторяющиеся цифры')
        if len(nums) !=4 or not nums.isdigit():
            continue
        nums = list(map(int, nums))
        if len(set(nums)) == 4:
            break
    return nums

# Сравниваем два числа и сообщаем количество быков и коров
def chek(nums, true_nums):
    bulls, cows = 0, 0
    for i, num in enumerate(nums):
        if num in true_nums:
            if nums[i] == true_nums[i]:
                bulls += 1
            else:
                cows += 1
    return bulls, cows


# Удаляем плохие ответы - не подходящие варианты из списка возможных
def del_bad_answers(ans, enemy_try, bull, cow):
    for num in ans[:]:
        tmp_bull, tmp_cow = chek(num, enemy_try)
        if tmp_bull != bulls or tmp_cow != cows:
            ans.remove(num)
    return ans


if '__name__' == '__main__':
    print('Игра быки и коровы')
    answers = get_all_answers()
    player = input_number()
    enemy = get_one_answer(answers)
    while True:
        print('=' * 15, 'Ход игрока', '=' * 15)
        print('Угадайте число компьютера')
        number = input_number()
        print(enemy)
        bulls, cows = chek(number, enemy)
        print(f'Быки: {bulls}, Коровы: {cows}')
        if bulls == 4:
            print("Победа!")
            print(f'Загаданное число - {enemy}')
            break
        enemy_try = get_one_answer(answers)
        print(f'Компьютер счиьтает, что вы загадали число: {enemy_try}')
        bulls, cows = chek(enemy_try, player)
        print(f'Быки: {bulls}, Коровы: {cows}')
        if bulls == 4:
            print("Победил компьютер!")
            print(f'Загаданное компьютером число - {enemy}')
            break
        else:
            answers = del_bad_answers(answers, enemy_try, bulls,  cows)