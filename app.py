from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import requests
import bs4
import os


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Result


    
def get_ticket_city(code):
    response = requests.get(
        "https://gpay.app.goo.gl/" + code)
    
    if "Dynamic Link Not Found" in response.text:
        return None
    
    html = bs4.BeautifulSoup(
        response.text, features="lxml")

    if "A special" not in html.title.text:
        return None

    return html.title.text.split(" ")[2]
    
    
    



@app.route('/collect')
def collect():
    # Endpoint to collect tickets
    code = request.args.get("code", "abcde")
    city = get_ticket_city(code)
    if city is None:
        return "Invalid Ticket"
    
    # TODO: Add to DB as unclaimed ticket if doesn't exist
    try:
        ticket = Result(code, city, False)
        db.session.add(ticket)
        db.session.commit()
        return "Ticket added. id={}".format(ticket.code)
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run()
# collect  - verify valid ticket and upsert to db
# admin claim - claim a ticket
# admin view - list all unclaimed ticket