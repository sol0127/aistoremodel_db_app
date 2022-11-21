from flask import Flask, request, render_template, redirect, url_for
import sys
app = Flask(__name__)
from aistore import *
from wtforms import Form, StringField, PasswordField, TextAreaField, validators



@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route("/sregister", methods=['POST', 'GET'])
def sregister():
    if request.method == 'POST':
        #
        s_id=request.form['sId']
        s_name=request.form['sName']
        s_locate=request.form['locate']
        pwd=request.form['sPassword']
        is_checked=request.form.get('aiotCheck')
        create_store(s_id,s_name,s_locate)
        print(request.method)
        print()
        return redirect('/')

    return render_template('sregister.html')

@app.route("/stores", methods=['POST', 'GET'])
def stores():
    if request.method == 'POST':
        #
        s_id=request.form['sId']
        return render_template('stores.html',stores=show_list(s_id))

    return render_template('stores.html', stores = show_list())

@app.route("/manage/<s_id>", methods=['POST', 'GET'])
def manage(s_id = 'nan'):
    if request.method == 'POST':
        pass

    return render_template('manage.html', s_id = s_id, )

@app.route("/board/<s_id>", methods=['POST', 'GET'])
def board(s_id = 'nan'):
    if request.method == 'POST':
        pass
    return render_template('board.html',
                           s_id=s_id)

if __name__ == '__main__':
    app.run('0.0.0.0',9999, debug=True)