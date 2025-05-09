# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.

import cx_Oracle
import sys
import json
import time

oracle_sql = '''SELECT * FROM hrm_attendance_info'''                      

def query_db(query, args=(), one=False):
    db_connection_info = 'user/pass@ip/sid'
    con = cx_Oracle.connect(db_connection_info)
    cur_oracle = con.cursor()
    cur_oracle.execute(query, args)
    r = [dict((cur_oracle.description[i][0], value) \
               for i, value in enumerate(row)) for row in cur_oracle.fetchall()]
    cur_oracle.connection.close()
    return (r[0] if r else None) if one else r
	

	
def attendance(request):
	my_query = query_db(oracle_sql)
	json_output = json.dumps(my_query)	
	return HttpResponse(json_output)   
    
