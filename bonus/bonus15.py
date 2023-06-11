# import csv
#
# FILEPATH = 'bonus15/questions.csv'
#
# with open(FILEPATH) as file:
#     data = list(csv.reader(file, delimiter=';'))
#
# count_question = data[1:].__len__()
# count_correct_answer = 0
#
# for question in data[1:]:
#     right_answer = question.pop(-1)
#     string_question = ''.join(string + '\n' for string in question)
#     print(string_question)
#     user_answer = input('Enter the correct answer: ')
#
#     if user_answer == right_answer:
#         count_correct_answer += 1
#
# print(f"You answered {count_correct_answer} out of {count_question} questions correctly")

# questions = [
#     {
#         'question_text': 'What are dolphins?',
#         'alternatives': [
#             'Amphibians',
#             'Fish',
#             'Mammals',
#             'Birds'
#         ],
#         'correct_answer': 3
#     },
#     {
#         'question_text': 'What occupies most of the Earth\' surface?',
#         'alternatives': [
#             'Land',
#             'Water',
#         ],
#         'correct_answer': 2
#     },
# ]
#
# count_user_corrent_answer = 0
# count_questions = questions.__len__()
#
# for question in questions:
#     # string_question = f"{question['question_text']}\n" + ''.join(f"{index}) {alternatives}\n" for index, alternatives in enumerate(question['alternatives']))
#     # print(string_question)
#     # user_answer = int(input('Enter the correct answer: '))
#     #
#     # if user_answer == (question['correct_answer'] - 1):
#     #     count_user_corrent_answer += 1
#
#     text_question = question['question_text'] + '\n'
#     string_question = ''
#
#     for index, alternatives in enumerate(question['alternatives']):
#         index += 1
#         if index == 1:
#             string_question = text_question
#
#         string_question += f"{index}) {alternatives}\n"
#
#     if string_question != '':
#         print(string_question)
#         user_answer = int(input('Enter the correct answer: '))
#         if user_answer == question['correct_answer']:
#             count_user_corrent_answer += 1
#
# print(f"You answered {count_user_corrent_answer} out of {count_questions} questions correctly")

import json

FILEPATH = 'bonus15/questions.json'

with open(FILEPATH) as file:
    content = file.read()

questions = json.loads(content)

count_user_corrent_answer = 0
count_questions = questions.__len__()

for question in questions:
    text_question = question['question_text'] + '\n'
    string_question = ''

    for index, alternatives in enumerate(question['alternatives']):
        index += 1
        if index == 1:
            string_question = text_question

        string_question += f"{index}) {alternatives}\n"

    if string_question != '':
        print(string_question)
        user_answer = int(input('Enter the correct answer: '))
        if user_answer == question['correct_answer']:
            count_user_corrent_answer += 1

print(f"You answered {count_user_corrent_answer} out of {count_questions} questions correctly")