from django.shortcuts import render
from django.http import HttpResponse
import time
from django.core.files import File
# Create your views here.


#import lets_convert
from django.shortcuts import render
#import mysql_test
import mysql.connector
import requests
import pymysql

def try_to_connect():
    cnx = pymysql.connect(user='root', password='secret',host='mysql-server',database='app1')



def traider(req):
    f = open("to_be_frontend_check_make_traid.html", "r")
    try_to_connect()
    output= f.read()
    f.close()
    return HttpResponse( output )



    



