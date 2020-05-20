from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# create Flask instance
app = Flask(__name__)

# use PyMongo to establish connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")


@app.route("/")
def home():
