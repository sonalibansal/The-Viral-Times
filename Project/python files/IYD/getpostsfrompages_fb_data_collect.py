# -*- coding: cp1252 -*-

import requests
import json
import pymysql

access_token = 'EAAHYJXZB5WPwBAPAZBpa8W0hlgOxvBFe24SzUczHihFadkdhP93obmlu99lfBMMCGlIBALOpQ2GXnnS6HXpjX9JaDUB5Dlny1eim2uPgX3cWafdZCe2ljBTiDTDPmKP4KxYEOZC4ZAFWL7Sm6oENUvEriZBe3x6OgZD'

def get_posts():
    con = pymysql.connect(user='root',password ='', database = 'youthfest_db',charset='utf8')
    cur = con.cursor()
    sql_create = "CREATE TABLE IF NOT EXISTS posts_details(page_id bigint unsigned, post_id varchar(100) NOT NULL PRIMARY KEY, created_time varchar(100),likes bigint unsigned, comments bigint unsigned)"
    cur.execute(sql_create)
    con.commit()
    sql = "SELECT page_id FROM Facebook_pages"
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        page_id = str(row[0])
        print "page id is"
        print page_id
        base_url = 'https://graph.facebook.com/v2.6/'+page_id+'/posts?limit=100&__paging_token=enc_AdBkVIKxLWOZCOJInFziNuBISLQfTQHZClNHM12ZBqvXYTa6FOQCcwo8ZBABQ8YGmonPtHrwduVv3aR8A7jtcjxDlkLeAgDaomllmjihe4ps3MCYdgZDZD&since=1417595768&__previous=1&access_token=EAAHYJXZB5WPwBAPAZBpa8W0hlgOxvBFe24SzUczHihFadkdhP93obmlu99lfBMMCGlIBALOpQ2GXnnS6HXpjX9JaDUB5Dlny1eim2uPgX3cWafdZCe2ljBTiDTDPmKP4KxYEOZC4ZAFWL7Sm6oENUvEriZBe3x6OgZD'
        for j in range(0,10):
            print "page"
            feed = json.loads(requests.get(base_url).text)
            for item in feed['data']:
                    post_id = str(item['id'])
                    print post_id
                    created_time = item['created_time']
                    base_url = 'https://graph.facebook.com/v2.6/'+post_id+'/likes?&summary=true&access_token=EAAHYJXZB5WPwBAPAZBpa8W0hlgOxvBFe24SzUczHihFadkdhP93obmlu99lfBMMCGlIBALOpQ2GXnnS6HXpjX9JaDUB5Dlny1eim2uPgX3cWafdZCe2ljBTiDTDPmKP4KxYEOZC4ZAFWL7Sm6oENUvEriZBe3x6OgZD'
                    datas = json.loads(requests.get(base_url).text)
                    tc = datas['summary']['total_count']
                    base_url = 'https://graph.facebook.com/v2.6/'+post_id+'/comments?&pretty=0&summary=true&access_token=EAAHYJXZB5WPwBAPAZBpa8W0hlgOxvBFe24SzUczHihFadkdhP93obmlu99lfBMMCGlIBALOpQ2GXnnS6HXpjX9JaDUB5Dlny1eim2uPgX3cWafdZCe2ljBTiDTDPmKP4KxYEOZC4ZAFWL7Sm6oENUvEriZBe3x6OgZD'
                    com = json.loads(requests.get(base_url).text)
                    comments = com['summary']['total_count']
                    sql_insert = "INSERT INTO posts_details(page_id,post_id,created_time,likes,comments)values ('%s','%s','%s','%s','%s')" % (page_id,post_id,created_time,tc,comments)
                    cur.execute(sql_insert)
                    con.commit()
            try:
                base_url = feed['paging']['next']
            except:
                break
    cur.close()
    con.close()
get_posts()
