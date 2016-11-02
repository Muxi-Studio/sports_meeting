# coding: utf-8

from flask import render_template,Flask,jsonify
import MySQLdb
import os, sys, string
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
HOST = os.environ.get("HOST")
USER = os.environ.get("USER")
PASSWD = os.environ.get("PASSWD")
DB = os.environ.get("DB")
db = MySQLdb.connect(host=HOST,user=USER,passwd=PASSWD,db=DB)

    
@app.route('/result/',  methods=['GET'])
def result():
    sql = "SELECT table1.Content1,table2.Content2, table3.Content3 FROM table1, table2, table3 ORDER BY rand() limit 1"
    cursor = db.cursor()
    r=cursor.execute(sql)
    alldata = cursor.fetchall()
    db.query = sql
    return jsonify({
        'result':alldata
    })

if __name__ == '__main__':
	app.run(debug=True)

