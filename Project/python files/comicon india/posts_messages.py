import requests
import json
import pymysql
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

access_token = 'EAAYUZByQgzIkBAAQwsYZCxXj9r33XSLz3kzE8w0E42eujH3LlsVevRFnpyjkyhYRGgyKhFg4mArox2HfYvobcLPYQo0efZB59tUGWbBnrCRe7vpPdXX71gP92QZAHUOZBxEBqzEqIGISdnCMTPWrbY2YggOvGcCkZD'

def get_feed():

    con = pymysql.connect(host='localhost',database='comic con india', user='root',charset='utf8mb4')
    cur = con.cursor()
    sql = "SELECT post_id FROM comicon_feeds"
    cur.execute(sql)
    rows = cur.fetchall()
    sql_create_table = "CREATE TABLE IF NOT EXISTS comicon_feed_messages(post_id varchar(100) NOT NULL PRIMARY KEY,message text)"
    cur.execute(sql_create_table)
    con.commit()
    print "Table created..."
    for row in rows:
        post_id = str(row[0])
        print post_id
        base_url ='https://graph.facebook.com/v2.6/'+post_id+'?limit=25&until=1401834693&__paging_token=enc_AdAeyYkjzX1tLJoB3x4JkoRtQ6qW9dd1jbDJZAadek3or8ZBvZARaSFCsjsxZBJsi5nqN6U4isMH3v5u3FOjAvC0QNw4P9mLnI2PaJxniTnDFFyVngZDZD&access_token=EAAHaG7wYo5ABACV5RR76FKwGGw5IZBa2FwW3Qo4YvKvXrwjzy5jeuXWaX7D2CxM7Ur4ogyDDlVRzfcw4wWuqMRPQ8Op29f5AanV15U2hm7Re6rdaMEOqf2nvDgbaOgbSq6YWWebBLQImGRz15PFkudmSqhqoZD'
        feed = json.loads(requests.get(base_url).text)
        if 'message' in feed: 
            message=feed['message']
            print feed['message']
        else:
            message =''
        sql_insert = "INSERT INTO comicon_feed_messages(post_id,message) values (%s,%s)"
        cur.execute(sql_insert,(post_id,message))
        con.commit()
        print "Post inserted."



    con.commit()
    cur.close()
    con.close()

get_feed()
