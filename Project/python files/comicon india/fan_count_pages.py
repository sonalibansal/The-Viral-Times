import requests
import json
import pymysql

access_token = 'EAAYUZByQgzIkBAAQwsYZCxXj9r33XSLz3kzE8w0E42eujH3LlsVevRFnpyjkyhYRGgyKhFg4mArox2HfYvobcLPYQo0efZB59tUGWbBnrCRe7vpPdXX71gP92QZAHUOZBxEBqzEqIGISdnCMTPWrbY2YggOvGcCkZD'

def get_likes():
    con = pymysql.connect(user='root',password ='', database = 'comic con india',charset='utf8')
    cur = con.cursor()
    sql = "SELECT id FROM comic_con_pages"
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        page_id = row[0]
        print "page id is"
        print page_id
        base_url = 'https://graph.facebook.com/v2.6/'+page_id+'?fields=fan_count&access_token=EAAHYJXZB5WPwBAPAZBpa8W0hlgOxvBFe24SzUczHihFadkdhP93obmlu99lfBMMCGlIBALOpQ2GXnnS6HXpjX9JaDUB5Dlny1eim2uPgX3cWafdZCe2ljBTiDTDPmKP4KxYEOZC4ZAFWL7Sm6oENUvEriZBe3x6OgZD'
        likes = json.loads(requests.get(base_url).text)
        fan = likes['fan_count']
        sql_insert = "INSERT INTO comic_fan_count_pages (page_id,page_name,fan_count) values ('%s','%s','%s')" % (page_id,page_name,fan)
        cur.execute(sql_insert)
        con.commit()

    cur.close()
    con.close()
get_likes()
