from flask import Flask, render_template, request
import random as Random
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("application.html",rand=str(Random.randint(0,1000000)))

@app.route('/aboutus')
def aboutus():
    return render_template("aboutus.html",rand=str(Random.randint(0,1000000)))

@app.route('/profile' , methods = ['GET', 'POST'])
def profile():
    if request.method == 'GET':
        return render_template("form.html")
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        print(name, age)
        return 'Request recieved ' + name


if __name__ == "__main__":
    app.run(debug=True,)