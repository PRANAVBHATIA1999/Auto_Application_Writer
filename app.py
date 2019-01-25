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
        selected_value = request.form['selected_value']
        f = writer.create(address, first_name, last_name, senders_class, rno, date_from, date_till, days, app_date, selected_value)
        f.seek(0)

        return send_file(f, as_attachment=True, attachment_filename='application.doc')

@app.route('/visaform', methods=['GET', 'POST'])
def visaform():
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
        country_name = request.form['country_name'] #NEW
        purp_visit = request.form['purp_visit'] #NEW
        app_date = request.form['app_date']
        selected_value = request.form['selected_value']
        f = writer.createVisaForm(address, first_name, last_name, senders_class, rno, date_from, date_till, app_date, purp_visit, country_name, selected_value)
        f.seek(0)

        return send_file(f, as_attachment=True, attachment_filename='application.doc')


@app.route('/participation', methods=['GET','POST'])
def participation():
        if request.method == 'GET':
                 return render_template("application.html", rand=str(Random.randint(0, 1000000)))
        if request.method == 'POST':
                address= request.form['address']
                first_name = request.form['fname']
                last_name = request.form['lname']
                senders_class = request.form['senders_cl']
                rno = request.form['rno']
                date_from = request.form['date_from']
                date_till = request.form['date_till']
                fest_name = request.form['fest_name']
                college_name_fest = request.form['college_name_fest']
                compet_name = request.form['compet_name']
                no_of_parti = request.form['no_of_parti']
                app_date = request.form['app_date']
                selected_value = request.form['selected_value']
                print(selected_value)
                f = writer.createPartiForm(address, first_name, last_name, senders_class, rno, date_from, date_till, fest_name, college_name_fest, compet_name, no_of_parti, app_date, selected_value)
                f.seek(0)

                return send_file(f, as_attachment=True, attachment_filename='application.doc')




# return render_template("application.html",rand=str(Random.randint(0,1000000)))


@app.route('/aboutus')
def aboutus():
    # rand_number = str(Random.randint(0, 1000000))
    return render_template("aboutus.html",rand=str(Random.randint(0, 1000000)))


@app.route('/contact')
def contactus():
    if request.method == 'POST':
        # request.form
        return

#Form UI designing

@app.route('/testing')
def testing():
      return render_template("form_testing.html",rand=str(Random.randint(0, 1000000)))


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
