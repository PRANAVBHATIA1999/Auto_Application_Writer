import os
import random as Random

from flask import Flask, render_template, request
from flask import make_response, send_file

import writer as writer

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def application():
    if request.method == 'GET':
        return render_template("application.html", rand=str(Random.randint(0, 1000000)))
    if request.method == 'POST':
        address = request.form['address']
        first_name = request.form['fname']
        last_name = request.form['lname']
        senders_class = request.form['senders_cl']
        rno = request.form['rno']
        date_from = request.form['date_from']
        date_till = request.form['date_till']
        days = request.form['no_days']
        app_date = request.form['app_date']
        f = writer.create(address, first_name, last_name, senders_class, rno, date_from, date_till, days, app_date)
        f.seek(0)

        return send_file(f, as_attachment=True, attachment_filename='application.doc')

        # Strings

        # para1 + address + brk +  para2 + app_date + para3 + para4 + para5a + days + para5b + date_from + to +
        # date_till + para5c + para6 + brk + first_name + space + last_name + brk + senders_class + brk + rno

        # next line

# return render_template("application.html",rand=str(Random.randint(0,1000000)))


@app.route('/aboutus')
def aboutus():
    rand_number = str(Random.randint(0, 1000000))
    return render_template("aboutus.html", rand_number)


@app.route('/contact')
def contactus():
    if request.method == 'POST':
        # request.form
        return



@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'GET':
        return render_template("form.html")
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        print(name, age)
        return 'Request recieved ' + name


if __name__ == "__main__":
    app.run(debug=True)
