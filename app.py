from flask import Flask, request, jsonify
# flask for api,request for input,jsomify for output
import pickle
# to load the saved model
app=Flask(__name__)
# creates flask app
model=pickle.load(open('model.pkl','rb'))
# to load the trained  model from model.pkl file

@app.route('/')
def home():
    return "Tonights the Night"


# prediction route 

@app.route('/predict',methods=['POST'])
def predict():

    # get data from request in json format
    data=request.json

    # extracts experience value from input
    exp=data['Experience']

    result=model.predict([[exp]])

    return jsonify({"salary":int(result[0])})

if __name__=='__main__':
    app.run(debug=True)