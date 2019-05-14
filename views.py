from flask import render_template, request, redirect, url_for
from flask import Flask


#app.run(debug=True)
app = Flask(__name__, template_folder = 'template') #__init__.py, 'template'
app.config.from_object('config')



@app.route('/')
def index():
    return render_template('index.html')