from flask import Flask, jsonify, request

app = Flask(__name__)
heart_rec = [
    {
        "heart_id": 0,
        "date" : "09/21/2022",
        "heartrate" : 90
    },
]

@app.route('/heart', methods=['GET'])

def getHeartRate():
    return jsonify(heart_rec)

@app.route('/heart', methods=['POST'])


def insertHeartRate():
    heartrate = request.get_json()
    heart_rec.append(heartrate)
    return {'id': len(heart_rec)},200


@app.route('/heartget', methods=['GET'])
def getSpecificHeartrecord():
    id_query = request.args.get('heart_id')
    return jsonify(heart_rec['heart_id' == id_query]),300

if __name__ == '__main__':
    app.run()