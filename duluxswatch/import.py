import sys
import json

import tinydb

db = tinydb.TinyDB('./db.json')
db.purge_tables()

data = json.load(sys.stdin)

print('Inserting {0} colours'.format(len(data['colors'])))

db.insert_multiple(data['colors'])
