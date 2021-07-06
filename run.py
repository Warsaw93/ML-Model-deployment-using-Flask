from flask import Flask, render_template
import pickle

from flask.globals import request
app = Flask(__name__)

@app.route('/', methods =['GET','POST'])
def home():
    if request.method == 'POST':
        model = pickle.load(open('lr_model.pkl', 'rb'))
        user_input = request.form.get('size')
        user_input=float(user_input)
        prediction = model.predict([[user_input]])
        print(prediction)
    return render_template('index.html', prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True)
