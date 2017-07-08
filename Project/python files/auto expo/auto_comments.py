import requests
import json
import pymysql
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

access_token = 'EAAHaG7wYo5ABACV5RR76FKwGGw5IZBa2FwW3Qo4YvKvXrwjzy5jeuXWaX7D2CxM7Ur4ogyDDlVRzfcw4wWuqMRPQ8Op29f5AanV15U2hm7Re6rdaMEOqf2nvDgbaOgbSq6YWWebBLQImGRz15PFkudmSqhqoZD'

def get_comments():

    con = pymysql.connect(host='localhost',database='auto expo', user='root',charset='utf8mb4')
    cur = con.cursor()
    sql = "SELECT page_id,post_id,created_time FROM Pages_Feed"
    cur.execute(sql)
    rows = cur.fetchall()
    sql_create_table = "CREATE TABLE IF NOT EXISTS Posts_comments (page_id bigint unsigned, post_id varchar(100) NOT NULL PRIMARY KEY,created_time timestamp,comments bigint unsigned)"
    cur.execute(sql_create_table)
    con.commit()
    print "Table created..."
    
    for row in rows:
        page_id = str(row[0])
        post_id = row[1]
        created_time= str(row[2])
        print page_id,post_id,created_time

        base_url='https://graph.facebook.com/v2.6/'+post_id+'/comments?pretty=0&summary=true&access_token=EAAHaG7wYo5ABACV5RR76FKwGGw5IZBa2FwW3Qo4YvKvXrwjzy5jeuXWaX7D2CxM7Ur4ogyDDlVRzfcw4wWuqMRPQ8Op29f5AanV15U2hm7Re6rdaMEOqf2nvDgbaOgbSq6YWWebBLQImGRz15PFkudmSqhqoZD'
        feed = json.loads(requests.get(base_url).text)
            
        
        comments=feed['summary']['total_count']
        
        print comments
        sql_insert = "INSERT INTO Posts_comments(page_id,post_id,created_time,comments) values (%s,%s,%s,%s)"
        cur.execute(sql_insert,(page_id,post_id,created_time,comments))
        con.commit()
        print "comments counted"
  
    
          



    cur.close()
    con.close()

get_comments()

