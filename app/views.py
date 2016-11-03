# coding: utf-8

from flask import render_template,Flask,jsonify
from app import app, db, basedir
    
@app.route('/result/',  methods=['GET'])
def result():
    alldata_encode = []
    sql = "SELECT table1.Content1,table2.Content2, table3.Content3 FROM table1, table2, table3 ORDER BY rand() limit 1"
    cursor = db.cursor()
    r=cursor.execute(sql)
    alldata = cursor.fetchall()
    # for datas in alldata:
    #     for data in datas:
    #         alldata_encode.append(data.decode('utf-8'))
    #db.query = sql
    return jsonify({
        'result':alldata
    })
