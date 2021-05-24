from flask import Flask
from faker import Faker
from flask import request
import requests
import csv

fake = Faker()
app = Flask(__name__)


@app.route('/requirements/')
def requirements():
    req = open(r'requirements.txt', 'r')
    rr = ''
    while True:
        line = req.readline()
        if not line:
            break
        rr += '<p>' + line.strip() + '</p>'
    req.close()
    return rr


@app.route('/generate-users/')
def fakes():
    a = int(request.args.get('count', 100))
    fn = ''
    for i in range(a):
        fn += '<p>' + fake.name().replace(' ', '') + '@gmail.com' + '</p>'
    return fn


@app.route('/mean/')
def h_w():
    with open('hw.csv', newline='') as csvfile:
        b = csv.reader(csvfile, delimiter=' ', quotechar='|')
        h = w = i = 0
        for row in b:
            if row != [] and row[1].replace(',', '').replace('.', '').isdigit():
                h += float(row[1].replace(',', ''))
                w += float(row[2].replace(',', ''))
                i += 1
        return '<p>Average height: ' + str(h/i*2.54) + ' cm' + '</p><p>Average weight: ' + str(w/i*0.453) + ' kg'


@app.route('/space/')
def cosmo():
    return 'Number of people: ' + str(requests.get('http://api.open-notify.org/astros.json').json()["number"])

