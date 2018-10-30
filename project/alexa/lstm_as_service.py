from flask import Flask, request


app = Flask(__name__)

model = None


@app.route('/home')
def doHome():
    return 'Hello, LSTM!'

@app.route('/train')
def doTrain():
    global model

    # Train the LSTM Model
    return 'It\'s Trained!'

@app.route('/predict')
def doPredict():
    if request.args.get('seed') == None:
        return "Please specify a seed parameter.  For example: http://my.example.com/?seed='rock the bells'"
   
    generated_text = "Model will output text"

    return str(generated_text)

# This will start a local WSGI instance
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443, debug=True, threaded=True, ssl_context=('MyCertificate.crt', 'MyKey.key'))
