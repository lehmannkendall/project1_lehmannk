from flask import Flask
from lab3_code import *

#what comes from URL values will be string

#set up Flask application
app = Flask(__name__)

#function that should occur at the home page
@app.route('/')
def welcome():
    return 'Welcome to the banking application!'

#path to return the bank name #TODO
@app.route('/bank/<name>')
def inst_bank_name(name):
    bank_name = Bank(name, Dollar)
    bank_name_s = bank_name.name
    return 'Welcome to {}!'.format(bank_name_s)

#path to return dollar amount
@app.route('/dollar/<amt>')
def inst_dollar(amt):
    dollar = Dollar(int(amt))
    dollar_s = dollar.__str__()
    return '{}'.format(dollar_s)

#path to return yuan amount
@app.route('/yuan/<amt>')
def inst_yuan(amt):
    yuan = Yuan(amt)
    yuan_s = yuan.__str__()
    return '{}'.format(yuan_s)

#path to return pound amount
@app.route('/pound/<amt>')
def inst_pound(amt):
    pound = Pound(int(amt))
    pound_s = pound.__str__()
    return '{}'.format(pound_s)

#TODO
#path to return information about bank instance
@app.route('/bank/<name>/<currency>/<value>')
def new_s(name, currency, value):

    if currency == "dollar":
        currency = Dollar
    elif currency == "pound":
        currency = Pound
    elif currency == "yuan":
        currency = Yuan
    else:
        return 'Invalid URL inputs for bank.'

    bank_inst = Bank(name, currency, int(value))
    bank_inst_s = bank_inst.__str__()
    return 'Welcome to the {} bank! {}.'.format(name, bank_inst_s)


if __name__ == "__main__":
    app.run()


# Something else to note is that the functions don't get INVOKED the way you may be used to. Running the application and *going to a URL that matches the path in the @app.route() business IS what runs that function!
