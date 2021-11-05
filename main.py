import requests
import os
import json
from flask import Flask, render_template, json, current_app as app, jsonify, request
from jinja2 import Environment, FileSystemLoader
app = Flask(__name__,template_folder='templates')

f_folder = 'js'
filename_ref='nytimes.html'
filename = 'index.html'
f_API = 'https://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7.json?api-key=9kQtsZaQ8kztIHcqijGuNW6yjYGu1FHv'

response = requests.get(f_API)
r = response.json()
nytimes = response.json()

fileLoader = FileSystemLoader('templates')
env = Environment(loader=fileLoader)

rendered = env.get_template('nytimes.html').render(data=nytimes, title='NY TIMES')

# Write HTML to a file - index.html

with open (f"./templates/{filename}","w",encoding='UTF-8') as f:
    f.write(rendered)

@app.route('/') 

def Index(): 
     return render_template(filename) 

if __name__ =='__main__': 
    app.run(debug=False)