import requests
import json
import pymysql

access_token = 'EAAHYJXZB5WPwBAPAZBpa8W0hlgOxvBFe24SzUczHihFadkdhP93obmlu99lfBMMCGlIBALOpQ2GXnnS6HXpjX9JaDUB5Dlny1eim2uPgX3cWafdZCe2ljBTiDTDPmKP4KxYEOZC4ZAFWL7Sm6oENUvEriZBe3x6OgZD'

def get_posts_likes():
    con = pymysql.connect(user='root',password ='', database = 'project',charset='utf8')
    cur = con.cursor()
    sql = "SELECT post_id FROM posts_details_iitf"
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        post_id = str(row[0])
        print "post_id is"
        print post_id
        base_url = 'https://graph.facebook.com/v2.6/'+post_id+'/likes?&summary=true&access_token=EAAHYJXZB5WPwBAPAZBpa8W0hlgOxvBFe24SzUczHihFadkdhP93obmlu99lfBMMCGlIBALOpQ2GXnnS6HXpjX9JaDUB5Dlny1eim2uPgX3cWafdZCe2ljBTiDTDPmKP4KxYEOZC4ZAFWL7Sm6oENUvEriZBe3x6OgZD'
        data = json.loads(requests.get(base_url).text)
        print data['summary']
        print data['summary']['total_count']
        tc = data['summary']['total_count']
        print tc
        sql_insert = "INSERT INTO posts_likes (post_id,likes) values ('%s','%s')" % (post_id,tc)
        cur.execute(sql_insert)
        con.commit()
        print "inserted value"
        
get_posts_likes()
