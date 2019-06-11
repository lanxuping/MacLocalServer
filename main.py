from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/lxp/go/')
def login_json():
    json_data = {'user':{'username':'warning'},'password':'123'}
    return jsonify(json_data)
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8088,debug=True)
