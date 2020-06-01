
from django.shortcuts import render
import pymysql
from django.http import JsonResponse
from .methods import *
import requests

class Database():
    def __init__(self, host, port, user, password, db, charset="utf8"):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.charset = charset
    def connect(self):
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password, db=self.db, charset=self.charset)
        self.cursor = self.conn.cursor()
    def get_all(self, sql, *args):
        try:
            self.connect()
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            self.cursor.close()
            self.conn.close()

    def get_one(self, sql):
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
            print(result)
        finally:
            self.cursor.close()
            self.conn.close()
        return result


def read_count(request):
    start_time = request.POST.get('start_time')
    end_time = request.POST.get('end_time')
    part_tag = request.POST.get('part_tag')
    item = request.POST.get('item')
    switcher = {
        1: tai_read_count,
        2: county_read_count,
        3: app_read_count,
    }
    method = switcher.get(part_tag)
    res = {}
    if method:
        result = method(start_time, end_time, item)
        res = {'status': 200, 'msg': result}
    return JsonResponse(res, safe=False)


