from crypt import methods
from project import app
from flask import render_template, redirect, url_for
"""
    Import MOdels
from project.models.Hello import Hello
"""
#route index
@app.route('/', methods = ['GET'])
def index():
    data = {
        "title": "Hello World",
        "body": "Flask simple MVC"
    }
    return render_template('index.html', data = data)
@app.route('/move',methods=['GET'])
def move():
    halaman ={
        "nama":"move to page 2",
        "status" : "successfull page 2"
    }
    return render_template('page2.html',halaman=halaman)
@app.route('/process',methods=['GET'])
def process():
    data = {
        "value1":"halaman process",
        "value2":"sukses masuk process"
    }
    return render_template('process.html',data=data)