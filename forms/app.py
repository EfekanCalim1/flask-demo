from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField, DecimalField, SubmitField
from datetime import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = '123456789'

class BasicForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    date = DateField('Date of birth')
    age = IntegerField('Age')
    decimal = DecimalField('Decimal')
    submit = SubmitField('Add Name')

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def register():
    error = ""
    form = BasicForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        date = form.date.data
        age = form.age.data
        decimal = form.decimal.data

        if len(first_name) == 0 or len(last_name) == 0:
            error = "Please supply both first and last name"
        else:
            return 'Thank you'
        if age < 0:
            return 'Please enter a real age'

    return render_template('home.html', form=form, message=error)

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0')
