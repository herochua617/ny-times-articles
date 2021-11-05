import requests
import os
import json
from dotenv import load_dotenv
from flask import Flask, render_template, json, current_app as app, jsonify, request
from jinja2 import Environment, FileSystemLoader

load_dotenv()

secret_key = os.getenv("API_KEY")
f_folder = os.getenv("f_folder")
filename_ref = os.getenv("filename_ref")
filename = os.getenv("filename")
f_API = "https://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7.json?api-key=" + secret_key
app = Flask(__name__,template_folder="templates")


@app.route('/') 

def Index(): 
    response = requests.get(f_API)
    r = response.json()
    nytimes = response.json()

    fileLoader = FileSystemLoader('templates')
    env = Environment(loader=fileLoader)
    rendered = env.get_template(filename).render(data=nytimes, title='NY TIMES')

    with open (f"./templates/{filename}","w",encoding='UTF-8') as f:
        f.write(rendered)

    return render_template(filename) 

if __name__ =='__main__': 
    app.run(debug=False)