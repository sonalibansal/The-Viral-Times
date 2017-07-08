import requests
import json
import pymysql

access_token = 'EAAHYJXZB5WPwBAPAZBpa8W0hlgOxvBFe24SzUczHihFadkdhP93obmlu99lfBMMCGlIBALOpQ2GXnnS6HXpjX9JaDUB5Dlny1eim2uPgX3cWafdZCe2ljBTiDTDPmKP4KxYEOZC4ZAFWL7Sm6oENUvEriZBe3x6OgZD'

def get_likes():
    con = pymysql.connect(user='root',password ='', database = 'workshop',charset='utf8')
    cur = con.cursor()
    sql = "SELECT page_id FROM Facebook_pages"
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        page_id = str(row[0])
        print "page id is"
        print page_id
        base_url = 'https://graph.facebook.com/v2.6/'+page_id+'?fields=fan_count&access_token=EAAHYJXZB5WPwBAPAZBpa8W0hlgOxvBFe24SzUczHihFadkdhP93obmlu99lfBMMCGlIBALOpQ2GXnnS6HXpjX9JaDUB5Dlny1eim2uPgX3cWafdZCe2ljBTiDTDPmKP4KxYEOZC4ZAFWL7Sm6oENUvEriZBe3x6OgZD'
        likes = json.loads(requests.get(base_url).text)
        fan = likes['fan_count']
        sql_insert = "INSERT INTO Facebook_pages (fan_count) values ('%s')" % fan
        cur.execute(sql_insert)
        con.commit()

    cur.close()
    con.close()
get_likes()
