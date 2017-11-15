import json
import os
import time
from sys import argv

from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

stub_response_folder_path = os.path.abspath(argv[1])


@app.route('/<path:url>', methods=['GET', 'POST'])
def get_sample_stub_response(url):
    print("Incoming request %s url: %s" % (request.method, request.url))
    print("Request body: %s", request.data)
    print("Request headers: %s", request.headers)
    response = get_file_contents(request.args.get('response_file'))
    return jsonify(response)

@app.route('/gojek/api/inquiry', methods=['GET', 'POST'])
def get_sample_inquiry_stub_response():
    print("Inquiry Stub : Incoming request %s url: %s" % (request.method, request.url))
    print("Request body: %s", request.data)
    print("Request headers: %s", request.headers)
    response = get_file_contents('inquiry_response')
    while True:
    	print("going to sleep")
    	time.sleep(5)
    	print("waking up from sleep")
    return jsonify(response)

@app.route('/auth', methods=['POST'])
def get_auth_response():
    response = make_response()
    response.headers['wallet_id'] = 'ww123'
    return response


def get_file_contents(stub_response_file_name):
    with open(os.path.join(stub_response_folder_path, stub_response_file_name + '.json'), mode='r') as response_data:
        json_data = json.load(response_data)
        return json_data


if __name__ == '__main__':
    app.run()
