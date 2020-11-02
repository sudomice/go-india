from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import requests
import bs4
import os


app = Flask(__name__)
# app.config.from_object(os.environ['APP_SETTINGS'])
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# from models import Result


    

    



@app.route('/collect')
def collect():
    # Endpoint to collect tickets
    code = request.args.get("code", "abcde")
    response = requests.get(
        "https://gpay.app.goo.gl/" + code)
    
    if "Dynamic Link Not Found" in response.text:
        return "Invalid ticket"
    
    html = bs4.BeautifulSoup(
        response.text, features="lxml")

    if "A special" not in html.title.text:
        return "Invalid ticket"
    
    print("https://gpay.app.goo.gl/" + code)
    city = html.title.text.split(" ")[2]
    # TODO: Add to DB as unclaimed ticket if doesn't exist

    


if __name__ == '__main__':
    app.run()
# collect  - verify valid ticket and upsert to db
# admin claim - claim a ticket
# admin view - list all unclaimed ticket