from string import Template

import tinydb
from flask import Flask

app = Flask(__name__)
db = tinydb.TinyDB('./db.json')

HTML = """<!DOCTYPE html>
    <html>
     <head>
      <title>${name} - Dulux Swatch</title>
      <link rel="StyleSheet" href="static/main.css" type="text/css">
     </head>
     <body style="background-color: rgb(${r}, ${g}, ${b})">${name}</div>
     </body>
    </html>
"""


@app.route('/<colour_id>')
def get_colour(colour_id):
    obj = db.get(tinydb.Query().id == colour_id)

    if not obj:
        obj = fetch_colour(colour_id)
        db.insert(obj)

    return Template(HTML).substitute(data)

def fetch_colour(colour_id):
    """
    Fetch RGB/name info from dulux
    """
    return {
        'id': colour_id,
        'name': 'mauve',
        'r': 100,
        'g': 20,
        'b': 50
    }
