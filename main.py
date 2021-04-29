from flask import Flask, jsonify, request, render_template, redirect
import requests

app = Flask(__name__, template_folder='templates')
app.static_folder = 'static'
LIABILITY_ENDPOINT = 'http://evergreen-env.eba-nm3pbh3f.us-east-1.elasticbeanstalk.com/api/liability'
types_list = ['Current','Non-current','Contingent']

@app.route('/',methods=['GET'])
def liabilitiesList():
    liabilities_list = requests.get(LIABILITY_ENDPOINT).json()
    return render_template('liabilityList.html', liabilities=liabilities_list)

@app.route('/createLiability',methods=['GET'])
def createLiability():
    return render_template('createLiability.html', types=types_list)

@app.route('/saveLiability',methods=['POST'])
def saveLiability():
    liabilityJson = dict(request.values)
    liabilityJson['precio'] = float(liabilityJson['value'])
    requests.post(LIABILITY_ENDPOINT, json=liabilityJson)
    return redirect('/')

@app.route('/deleteLiability/<id>')
def deleteLiability(id):
    requests.delete(LIABILITY_ENDPOINT + '/' +id)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')