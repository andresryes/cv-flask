#FLASK
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)
import os,optparse
import yaml

# developer = os.getenv("DEVELOPER", "Me")
environment=os.getenv("ENVIRONMENT","development")

with open("info.yml", 'r',encoding='utf-8') as stream:
    try:
        info = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

@app.route("/")
def about():
    return render_template("about.html", info=info)

@app.route("/academic")
def academic():
    return render_template("academic.html", info=info['academic'])

@app.route("/experience")
def experience():
    return render_template("experience.html", info=info['experience'])

@app.route("/social")
def social():
    return render_template("social.html", info=info['social'])

if __name__ == "__main__":
    debug=False
    if environment == "development" or environment == "local":
        debug=True
    app.run(host="0.0.0.0",debug=debug)
