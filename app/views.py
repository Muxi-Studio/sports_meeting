# coding: utf-8

from flask import render_template,Flask,jsonify
from app import app, db, basedir
    
@app.route('/result/',  methods=['GET'])
def result():
    alldata_encode = []
    # sql1 = "SELECT table1.Content1,table2.Content2, table3.Content3 FROM table1, table2, table3 ORDER BY rand() limit 1"
    sql1 = "SELECT Content1 from table1 ORDER BY rand() limit 1"
    sql2 = "SELECT Content2 from table2 ORDER BY rand() limit 1"
    sql3 = "SELECT Content3 from table3 ORDER BY rand() limit 1"
    cursor = db.cursor()
    cursor.execute(sql1); r1 = cursor.fetchall()
    r2=cursor.execute(sql2); r2 = cursor.fetchall()
    r3=cursor.execute(sql3); r3 = cursor.fetchall()
    alldata = r1[0] + r2[0] + r3[0]
    for data in alldata:
        try:
            alldata_encode.append(data.decode('utf-8'))
        except UnicodeDecodeError:
            pass
    #db.query = sql
    return jsonify({
        # 'result':alldata_encode
	'result': alldata_encode[0] + alldata_encode[1] + alldata_encode[2]
    })
