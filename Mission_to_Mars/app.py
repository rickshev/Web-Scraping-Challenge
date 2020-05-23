from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# create Flask instance
app = Flask(__name__)

# use PyMongo to establish connection
# mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


@app.route("/")
def home():

    # find data from mongo database
    mars = mongo.db.collection.find_one()

    # return template and data
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():

    mars = mongo.db.collection
    
    mars_info = scrape_mars.scrape()
    mars_info = scrape_mars.mars_image()
    # mars_info = scrape_mars.mars_weather()
    mars_info = scrape_mars.mars_facts()
    mars_info = scrape_mars.mars_hemispheres()

    mars.update({}, mars_info, upsert=True)
    
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)