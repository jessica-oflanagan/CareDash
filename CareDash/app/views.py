from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy
import sys

from app import app
db = SQLAlchemy(app)

class Provider_Info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    # profession = db.Column(db.String(50))
    # REVIEWS WOULD GO HERE #

# Main page access
@app.route('/')
def home():
    result = Provider_Info.query.all()
    return render_template("home.html")

# Processes provider template
@app.route('/process', methods=['POST'])
def process():
    name = request.form['firstname']
    provider = Provider_Info(name="HELLO")
    db.session.add(provider)
    db.session.commmit()
    return render_template("home.htl")
# 