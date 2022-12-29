import requests, html
import random as rd

def get_data(parameters):
    response = requests.get(url="https://opentdb.com/api.php", params=parameters)
    question_data = response.json()["results"] # Gets the data as a json object
    return process_questions(question_data)

# Index of all the categories available on opentdb.com
CATEGORIES = {
    "Entertainment: Music" : 12,
    "Entertainment: Television" : 14,
    "Entertainment: Video Games" : 15,
    "Science & Nature" : 17,
    "Science: Computers" : 18,
    "Science: Mathematics" : 19,
    "Sports": 21,
    "Science: Gadgets": 30,
    "Entertainment: Japanese Anime & Manga": 31
}

def get_category(stri):
    return CATEGORIES[stri]

def process_questions(question_data):
    question_bank = []
    for question in question_data:
        choices = []
        question_text = html.unescape(question["question"])
        correct_answer = html.unescape(question["correct_answer"])
        incorrect_answers = question["incorrect_answers"]
        for ans in incorrect_answers:
            choices.append(html.unescape(ans))
        choices.append(correct_answer)
        rd.shuffle(choices)
        new_question = [question_text, correct_answer, choices]
        question_bank.append(new_question)
    return question_bank
