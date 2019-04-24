import pendulum
import uuid
from flask import Flask, jsonify

app = Flask(__name__)


def get_utc_timestamp():
    return pendulum.now('UTC')

def format_utc_ts(utc_ts):
    pass
# END


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/utctime', methods=['GET'])
def get_utc_time():
    return jsonify({'UTC_TS': get_utc_timestamp()})


@app.route('/uuid', methods=['GET'])
def get_uuid():
     return jsonify({'UUID': uuid.uuid4()})


if __name__ == '__main__':
    app.run()
