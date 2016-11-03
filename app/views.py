# coding: utf-8

from flask import render_template,Flask,jsonify
from app import app, db, basedir
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')
    
@app.route('/result/',  methods=['GET'])
def result():
    alldata_encode = []
    # sql1 = "SELECT table1.Content1,table2.Content2, table3.Content3 FROM table1, table2, table3 ORDER BY rand() limit 1"
    sql1 = "SELECT Content1 from table1 ORDER BY rand() limit 1"
    sql2 = "SELECT Content2 from table2 ORDER BY rand() limit 1"
    sql3 = "SELECT Content3 from table3 ORDER BY rand() limit 1"
    cursor = db.cursor()
    cursor.execute("SET NAMES UTF8")
    cursor.execute(sql1); r1 = cursor.fetchall()
    r2=cursor.execute(sql2); r2 = cursor.fetchall()
    r3=cursor.execute(sql3); r3 = cursor.fetchall()
    # try:
    #     r1[0].encode('utf-8')
    # except UnicodeDecodeError:
    #     pass
    #db.query = sql
    all_data = r1[0] + r2[0] + r3[0]
    for data in all_data:
	alldata_encode.append(data.encode('utf-8'))
#         try:
#             alldata_encode.append(data.encode('utf-8'))
#         except UnicodeDecodeError:
#             # alldata_encode.append("xxxxxx")
#  	    alldata_encode.append(unicode(data, errors='replace'))
# 	    # alldata_encode.append(data.decode('gb2312').encode('utf-8'))
    return jsonify({
        # 'result': all_data[0] + all_data[1] + all_data[2]
	# 'result': alldata_encode[0] + alldata_encode[1] + alldata_encode[2]
	'result': alldata_encode[0] + alldata_encode[1] + alldata_encode[2]
    })
