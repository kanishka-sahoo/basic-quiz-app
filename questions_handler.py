import requests

def get_data(parameters):
    response = requests.get(url="https://opentdb.com/api.php", params=parameters)
    question_data = response.json()["results"] # Gets the data as a json object
    return question_data
