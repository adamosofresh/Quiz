import requests

ENDPOINT = "https://opentdb.com/api.php"
PARAMETERS = {
    "amount": 10,
    "type": "boolean"
}



response = requests.get(url=ENDPOINT, params=PARAMETERS)
response.raise_for_status()
questions = response.json()
question_data = questions["results"]
