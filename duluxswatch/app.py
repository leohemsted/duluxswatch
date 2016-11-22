from string import Template

import tinydb
import requests
from flask import Flask

app = Flask(__name__)
db = tinydb.TinyDB('./db.json')

HTML = """<!DOCTYPE html>
<html>
  <head>
    <title>Dulux Swatch</title>
    <link rel="StyleSheet" href="/static/main.css" type="text/css">
  </head>
  <body style="background-color: #${rgb}">
    <div>
        ${name}
        <br/>
        (id: <a href="https://www.dulux.co.uk/en/products/colour-tester#?selectedColor=${id}">${id}</a>)
    </div>
  </body>
</html>
"""

@app.route('/id/<colour_id>')
def get_colour_by_id(colour_id):
    obj = db.get(tinydb.Query().id == colour_id)

    if not obj:
        obj = fetch_colour(colour_id)
        from pprint import pprint
        pprint(obj)
        db.insert(obj)

    return Template(HTML).substitute(obj)

def fetch_colour(colour_id):
    """
    Fetch RGB/name info from dulux
    """
    response = requests.get('https://www.dulux.co.uk/en/api/color/{0}'.format(colour_id))
    response.raise_for_status()

    return response.json()
