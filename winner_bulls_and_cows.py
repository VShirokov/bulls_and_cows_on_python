import Bulls_and_cows

answers = Bulls_and_cows.get_all_answers()
counter = 0
bulls = 0
while len(answers) > 1 or bulls == 4:
    counter += 1
    print(f'Ход номер: {counter}')
    print(f'Возможных вариантов ответа: {len(answers)}')
    ans = Bulls_and_cows.get_one_answer(answers)
    print(f'Назови комбинацию: {ans}')
    bulls = int(input('Сколько быков?'))
    cows = int(input('Сколько коров?'))
    answers = Bulls_and_cows.del_bad_answers(answers, ans, bulls, cows)
print(f'Ответ: {answers}')