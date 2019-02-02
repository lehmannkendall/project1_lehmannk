from flask import Flask
from lab3_code import *

app = Flask(__name__)

@app.route('/home page/')
def welcome():
    return 'Welcome to the banking application!'

@app.route('/bank/<name>')
def inst_bank_name(name):
    #return inst_bank_name.__repr__()
    return 'Welcome to {}!'.format(name)

@app.route('/dollar/<amt>')
def inst_dollar(amt):
    # return '{}'.format(int(amt))
    dollar = Dollar(int(amt))
    dollar_s = dollar.__str__()
    return '{}'.format(dollar_s)
#what comes from URL values will be string

@app.route('/yuan/<amt>')
def inst_yuan(amt):
    yuan = Yuan(amt)
    yuan_s = yuan.__str__()
    return '{}'.format(yuan_s)

    # yuan = Yuan(int(amt))
    # return '{}'.format(yuan)

@app.route('/pound/<amt>')
def inst_pound(amt):
    pound = Pound(int(amt))
    pound_s = pound.__str__()
    return '{}'.format(pound_s)

@app.route('/bank/<name>/<currency>/<value>')
def new_s(name, currency, value):
    if currency == "dollar":
        currency = Dollar()
    elif currency == "pound":
        currency = Pound()
    elif currency == "yuan":
        currency = Yuan()
    else:
        return 'Invalid URL inputs for bank.'
    else:
        bank_inst = Bank(name, currency, int(value))
        bank_inst_s = bank_inst.__str__()
        return 'Welcome to the {} bank! {}.'.format(name, bank_inst_s)


if __name__ == "__main__":
    app.run()
