#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import httplib
import json


def get_json(game_id):
    conn = httplib.HTTPConnection("sports.media.daum.net")
    # http://sports.media.daum.net/ronaldo/gallery/view.json?id=283915
    target_url = 'http://sports.media.daum.net/ronaldo/gallery/view.json?id=' + game_id
    conn.request("GET", target_url)
    response = conn.getresponse()
    result_data = response.read()
    conn.close()
    return result_data

# Daum sports
game_number = "301744"
json = json.loads(get_json(game_number))

conn = sqlite3.connect(':memory:')
curr = conn.cursor()
curr.execute('create table table_for_sort ( id int, title text, link text )')
conn.commit()

for data in json['data']['gallery']['mediaRelations']:
    id = str(data['media']['id'])
    link = 'http://m.live.sports.media.daum.net/video/kbo/' + game_number + '/' + str(data['media']['id'])
    title = data['media']['fieldValues']['title']
    # print(id, title, link)
    curr.execute("""
    insert into table_for_sort
    (
    id, title, link
    ) values (
       """ + id + """
    , '""" + title.replace("'", '"') + """'
    , '""" + link + """'
    )""")
    conn.commit()

curr.execute('select * from table_for_sort order by id')
for row in curr.fetchall():
    # print(row[0])
    print("- " + row[1])
    print("  - " + row[2])

