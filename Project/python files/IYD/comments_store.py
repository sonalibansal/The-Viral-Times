import requests
import json
import pymysql

access_token = 'EAAHYJXZB5WPwBAPAZBpa8W0hlgOxvBFe24SzUczHihFadkdhP93obmlu99lfBMMCGlIBALOpQ2GXnnS6HXpjX9JaDUB5Dlny1eim2uPgX3cWafdZCe2ljBTiDTDPmKP4KxYEOZC4ZAFWL7Sm6oENUvEriZBe3x6OgZD'

def get_posts_comments():
    con = pymysql.connect(user='root',password ='', database = 'workshop',charset='utf8')
    cur = con.cursor()
    sql = "SELECT post_id FROM posts_details"
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        post_id = str(row[0])
        print "post_id is"
        print post_id
        base_url = 'https://graph.facebook.com/v2.6/'+post_id+'/comments?access_token=EAAHYJXZB5WPwBAPAZBpa8W0hlgOxvBFe24SzUczHihFadkdhP93obmlu99lfBMMCGlIBALOpQ2GXnnS6HXpjX9JaDUB5Dlny1eim2uPgX3cWafdZCe2ljBTiDTDPmKP4KxYEOZC4ZAFWL7Sm6oENUvEriZBe3x6OgZD'
        for i in range(0,10):
            feed = json.loads(requests.get(base_url).text)
            print feed
            for item in feed['data']:
                if 'message'in item:
                    print comments
                else:
                    comments = 'NULL'
                sql_insert = "INSERT INTO posts_comments(post_id,comments) values ('%s','%s')"
                cur.execute(sql_insert,(post_id,item['message']))
                con.commit()
            try:
                base_url = feed['paging']['next']
            except:
                break
            
            
        
    cur.close()
    con.close()
get_posts_comments()
            
