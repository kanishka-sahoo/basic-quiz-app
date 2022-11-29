import requests

parameters = {
    "amount": 15,
    "type": "multiple",
    "category": "18",
    "difficulty": "easy"
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
question_data = response.json()["results"]