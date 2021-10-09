# Call this api (http://api.plos.org/search?q=title:DNA)

# 1) load the data into database
# 2) load data into csv
# 3) only fetch 2017 year data and store into a json

import requests
import psycopg2
import copy
import unicodedata
import csv
from datetime import datetime
import json

response = requests.get("http://api.plos.org/search?q=title:DNA")

publication_list = response.json()["response"]["docs"]

#1)

conn = psycopg2.connect(
    host='ec2-52-204-213-254.compute-1.amazonaws.com', port=5432, user='nzidckngibagnw', dbname='d7guhevmgagv5q',
    password='a1f9301229bb8f7dac06d8c29c7c75b3ffac102f60a58e71e1687757a0bce690')

cur = conn.cursor()

sql_statment = "drop table if exists pyclass.dna_publications_di;"

cur.execute(sql_statment)

conn.commit()

sql_statment = """
create table pyclass.dna_publications_di (
id varchar(255) primary key,
journal varchar(255),
eissn varchar(255),
publication_date timestamp(1) without time zone,
article_type varchar(255),
author_display varchar(255)[],
abstract varchar(5000)[],
title_display varchar(255),
score numeric(9,7)
);
"""

cur.execute(sql_statment)

conn.commit()

sql_statment_frame = "insert into pyclass.dna_publications_di values ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', {});"

for item in publication_list:
    
    id_value = item["id"]
    journal_value = item["journal"]
    eissn_value = item["eissn"]
    publication_date_value = item["publication_date"]
    article_type_value = item["article_type"]
    author_display_value = "{" + ", ".join([f"\"{author}\"" for author in item["author_display"]]) + "}"
    abstract_value = "{" + ", ".join([f"\"{text}\"" for text in item["abstract"]]) + "}"
    title_display_value = item["title_display"]
    score_value = item["score"]
    
    sql_statment = sql_statment_frame.format(id_value,
                                             journal_value,
                                             eissn_value,
                                             publication_date_value,
                                             article_type_value,
                                             author_display_value,
                                             abstract_value,
                                             title_display_value,
                                             score_value)
    
    cur.execute(sql_statment)
    
conn.commit()

#2)

publication_list_copy = copy.deepcopy(publication_list)

for item in publication_list_copy:
    
    # Some characters cannot be directly written into .csv file.
    # We need to encode the text with utf-8.
    # When reading the .csv, we need to decode with utf-8.
        
    item['author_display'] = ",".join(item['author_display']).encode('utf-8')
        
    item['abstract'] = "|".join(item['abstract']).replace('\n', '\\n').encode('utf-8')

with open('dna_publications.csv', 'w', newline='') as f:
    
    col_names = [key for key in publication_list_copy[0]]
    
    writer = csv.DictWriter(f, fieldnames=col_names)

    writer.writeheader()
    
    for item in publication_list_copy:
        
        writer.writerow(item)

#3)

publication_list_copy = copy.deepcopy(publication_list)

for item in publication_list:
    
    if datetime.strptime(item["publication_date"], '%Y-%m-%dT%H:%M:%SZ').year != 2017:
        
        publication_list_copy.remove(item)
        
with open("dna_publications_2017.json", "w") as f:
    
    json.dump(publication_list_copy, f)