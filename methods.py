import pymysql
from .views import Database
def tai_read_count(start_time, end_time, item):
    db = Database(host="10.10.10.240", port=5432, user="root", password="tF!e5UN?iGMRkB7Z80Ln#O@uCsP^mS", db="dj_analytics")
    params = []
    start_time = start_time
    end_time = end_time
    dp = item
    sql = "select sum(read_count) from views_article where editor like'%%%s%%' and (pub_date between '%s' and '%s');" % (dp, start_time, end_time)
    params.append(start_time)
    params.append(end_time)
    r = db.get_all(sql)
    return r
def county_read_count(start_time, end_time, item):
    db = Database(host="10.10.10.240", port=5432, user="root", password="tF!e5UN?iGMRkB7Z80Ln#O@uCsP^mS", db="dj_analytics")
    start_time = start_time
    end_time = end_time
    county = item
    sql = "select sum(read_count) from views_article where region like '%%%s%%' and (pub_date between '%s' and '%s');" % (county, start_time, end_time)
    r = db.get_all(sql)
    return r

def app_read_count(start_time, end_time, item):
    db = Database(host="10.10.10.240", port=5432, user="root", password="tF!e5UN?iGMRkB7Z80Ln#O@uCsP^mS", db="dj_analytics")
    start_time = start_time
    end_time = end_time
    app_item = item
    sql = "select sum(read_count) from views_article where category='%s' and (pub_date between '%s' and '%s');" % (app_item, start_time, end_time)
    r = db.get_all(sql)
    return r