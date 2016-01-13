from os import environ

import requests
from flask import Flask
from flask.ext.cors import CORS
from flask.json import jsonify

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
# You can get API_KEY from here: https://www.explara.com/a/account/manage/app-settings
# Your API_KEY = '<YourKeyHere>'
API_KEY = environ['API_KEY']
TICKETS_URL = 'https://www.explara.com/api/e/get-tickets'
# EVENT_ID you can get via this request: https://www.explara.com/api/e/get-all-events
EVENT_ID = environ['EVENT_ID']


@app.route('/api/tickets-left/')
def get_remaining_tickets_count():
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': "Bearer %s" % API_KEY}
    payload = {'eventId': EVENT_ID}
    response = requests.post(TICKETS_URL, data=payload, headers=headers)
    data = response.json()
    try:
        data_response = {
            'tickets_left': data["tickets"][0]["quantity"]
        }
    except KeyError:
        return jsonify(**data)
    return jsonify(**data_response)


if __name__ == "__main__":
    app.run(debug=True)
