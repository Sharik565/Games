import json
import random


def krutite_baraban():  # имитация вращения барабана, возвращаемый результат - баллы. РАБОТАЕТ!!!
    lst = [100, 150, 200, 250, 300, 350, 400, 450, 500]
    random.shuffle(lst)
    points = lst[0]
    return points


def get_question():  # подтягивает список вопросов из файла, вопрос - словарь, где ключ - ответ, значение- вопрос.
    with open('questions.json', 'r', encoding='utf-8') as voprosy:
        voprosy = json.load(voprosy)
    random.shuffle(voprosy)
    return voprosy[0]


def correct_answer(question):
    answer_lst = list(question.keys())
    answer_lst = list(answer_lst[0])
    return answer_lst


def ask_question(question):
    return question.values()
