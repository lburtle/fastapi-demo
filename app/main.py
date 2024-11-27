#!/usr/bin/env python3

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import json
import os
import mysql.connector
from mysql.connector import Error

DBHOST = os.getenv('DBHOST')
DBUSER = os.getenv('DBUSER')
DBPASS = os.getenv('DBPASS')
DB = "xfd3tf_dp1"

db = mysql.connector.connect(user=DBUSER, host=DBHOST, password=DBPASS, database=DB)
cur=db.cursor()

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/genres')
def get_genres():
    db = mysql.connector.connect(user=DBUSER, host=DBHOST, password=DBPASS, database=DB)
    cur=db.cursor()
    query = "SELECT * FROM genres ORDER BY genreid;"
    try:    
        cur.execute(query)
        headers=[x[0] for x in cur.description]
        results = cur.fetchall()
        json_data=[]
        for result in results:
            json_data.append(dict(zip(headers,result)))
        return(json_data)
        cur.close()
        db.close()
    except Error as e:
        cur.close()
        db.close()
        return {"Error": "MySQL Error: " + str(e)}

@app.get('/songs')
def get_songs():
    db = mysql.connector.connect(user=DBUSER, host=DBHOST, password=DBPASS, database=DB)
    cur=db.cursor()
    query = "SELECT * FROM songs ORDER BY id;"
    try:    
        cur.execute(query)
        headers=[x[0] for x in cur.description]
        results = cur.fetchall()
        json_data=[]
        for result in results:
            json_data.append(dict(zip(headers,result)))
        return(json_data)
        cur.close()
        db.close()
    except Error as e:
        cur.close()
        db.close()
        return {"Error": "MySQL Error: " + str(e)}


