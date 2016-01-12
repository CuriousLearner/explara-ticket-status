from flask import Flask, Response
from os import environ
from json import dumps
import requests

app = Flask(__name__)
# You can get API_KEY from here: https://www.explara.com/a/account/manage/app-settings
# Your API_KEY = 'Bearer <YourKeyHere>'
API_KEY = environ['API_KEY']
TICKETS_URL = 'https://www.explara.com/api/e/get-tickets'
# EVENT_ID you can get via this request: https://www.explara.com/api/e/get-all-events
EVENT_ID = environ['EVENT_ID']

@app.route('/api/tickets-left/')
def get_remaining_tickets_count():
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': API_KEY}
    payload = {'eventId': EVENT_ID}
    response = requests.post(TICKETS_URL, data=payload, headers=headers)
    return Response(dumps({"tickets_left": response.json()["tickets"][0]["quantity"]}),
                                status=200,
                                content_type="application/json")

app.run(debug=True)
