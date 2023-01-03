"""
Questions Handler:
Accesses the opentdb.com api and gets the questions as per specifications
Contains a list of categories and their ids available
Shuffles the questions and their options collected.
"""

import requests, html
import random as rd

def get_data(parameters):
    # Check fot internet access and handle eventual error by returning string
    try:
        response = requests.get(url="https://opentdb.com/api.php", params=parameters)
    except requests.exceptions.ConnectionError:
        return "NoInternetError"

    # Parse the request data into a JSON format
    question_data = response.json()["results"] # Gets the data as a json object
    return process_questions(question_data)

# Index of some of the categories available on opentdb.com giving the name and number
CATEGORIES = {
    "Entertainment: Books": 10,
    "Entertainment: Music" : 12,
    "Entertainment: Television" : 14,
    "Entertainment: Video Games" : 15,
    "Science & Nature" : 17,
    "Science: Computers" : 18,
    "Science: Mathematics" : 19,
    "Sports": 21,
    "Geography": 22,
    "History": 23,
    "Politics": 24,
    "Celebrities": 26,
    "Vehicles" :28,
    "Science: Gadgets": 30,
    "Entertainment: Japanese Anime & Manga": 31
}

def get_category(stri): # Returns category number of category
    return CATEGORIES[stri]

def process_questions(question_data):   # Converts given JSON question format into a nested list
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
    rd.shuffle(question_bank)
    return question_bank
