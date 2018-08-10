from flask import Flask, render_template, request
import random as Random
app = Flask(__name__)

@app.route('/' , methods= ['GET' , 'POST' ])
def application():

    if request.method == 'GET':
        return render_template("application.html", rand=str(Random.randint(0,1000000)))
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
            # Strings
        para1 = 'The Dean <br> <br>'
        para2 = 'Date:'
        para3 = '<br> <br>  Subject: Leave application <br> <br>'
        brk = '<br>'
        para4 = 'Respected Sir/Ma’am,<br> <br>'
        para5a = 'I request to state that due to sudden illness I will not be able to attend school/college for'
        para5b = 'days as the doctor has advised me to take the required amount of rest.<br>  I hope to recover soon and make up for the irregularity in studies occurred.<br> I will return to school/college as a healthy student and take due care that my work and performance do not suffer.<br>  On the account of my sickness, I request you to kindly grant me leave from'
        to = 'to'
        space = ' '
        para5c = 'I shall be utterly obliged for this. <br> <br>'
        para6 = 'Yours obediently,'
        print(address, first_name, last_name, senders_class, rno,  date_from, date_till, days, app_date)
        return para1 + address + brk +  para2 + app_date + para3 + para4 + para5a + days + para5b + date_from + to + date_till + para5c + para6 + brk + first_name + space + last_name + brk + senders_class + brk + rno
       

        #next line 
# shitttt, kal 1-2 hrs waste kiye. 
# will HTML tages work here?? yes
# damnn, thankss np bye
        

        
    # return render_template("application.html",rand=str(Random.randint(0,1000000)))

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