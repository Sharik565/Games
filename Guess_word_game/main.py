import functions as f

points = 0

print('Вас приветствует игра "ПОЛЕ ЧУДЕС"!')
print()
print('Введите свое имя:')

name = input().title()

print()
print(f"Здравствуйте, {name}!")
print()

print('Внимание! Вопрос!')

lst_voprosov = f.get_question()
vopros, otvet = f.ask_question(lst_voprosov), f.correct_answer(lst_voprosov)
print(*vopros)
word = ['*' for i in range(len(otvet))]
print("".join(word))
print()

while "*" in word:
    print(f"{name}, вращайте барабан, нажав Enter!")
    input()
    ball = f.krutite_baraban()
    print(f"{ball} очков на барабане. Введите букву или слово")
    user_answer = input().upper().replace(' ', '')
    user_answer_lst = []
    if len(user_answer) > 1:
        for i in range(len(user_answer)):
            user_answer_lst.append(user_answer[i])
        user_answer = user_answer_lst
        for i in range(0, len(otvet)):
            if user_answer[i] == otvet[i] and user_answer[i] != word[i]:
                word[i] = otvet[i]
                points += ball

    elif len(user_answer) == 1:
        if user_answer in otvet:
            print('Вы угадали!')
            for i in range(0, len(otvet)):
                if user_answer == otvet[i]:
                    word[i] = otvet[i]
                    points += ball
            print(*word)
            print(f"{name}, у вас теперь {points} очков.")
        else:
            print('К сожалению, такой буквы нет. Попробуйте еще раз!')

print(word)
print(f"{name}, у вас теперь {points} очков.")
print(f"поздравляю, {name}! Вы выиграли!")
