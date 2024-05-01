import os
import psycopg
from dotenv import load_dotenv
from flask import Flask, render_template, request, url_for, flash, redirect
from zenpy import Zenpy
load_dotenv()
creds = {
    'email': os.environ.get("ZDUSERNAME"),
    'password': os.environ.get("ZDPASSWORD"),
    'subdomain': os.environ.get("ZDSUBDOMAIN")
}
zenpy_client = Zenpy(**creds)
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET")
parameters = [{'content': 'Last queries'}]
@app.route('/')
def index():
    return render_template('index.html', parameters=parameters)
@app.route('/query/', methods=('GET', 'POST'))
def query():
    if request.method == 'POST':
        content = request.form['content']
        if not content:
            flash('Parameters are requered!')
        else:
            parameters.append({'content': content})
            return redirect(url_for('index'))
    return render_template('query.html')
