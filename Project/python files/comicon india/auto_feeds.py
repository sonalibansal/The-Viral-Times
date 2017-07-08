import requests
import json
import pymysql
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

access_token = 'EAAHaG7wYo5ABACV5RR76FKwGGw5IZBa2FwW3Qo4YvKvXrwjzy5jeuXWaX7D2CxM7Ur4ogyDDlVRzfcw4wWuqMRPQ8Op29f5AanV15U2hm7Re6rdaMEOqf2nvDgbaOgbSq6YWWebBLQImGRz15PFkudmSqhqoZD'

def get_feed():

    con = pymysql.connect(host='localhost',database='comic con india', user='root',charset='utf8mb4')
    cur = con.cursor()
    sql = "SELECT page_id,page_name FROM comicon_pages"
    cur.execute(sql)
    rows = cur.fetchall()
    sql_create_table = "CREATE TABLE IF NOT EXISTS comicon_feeds (page_id bigint unsigned, post_id varchar(100) NOT NULL PRIMARY KEY,created_time timestamp,message text,post_num bigint)"
    cur.execute(sql_create_table)
    con.commit()
    print "Table created..."
    k=1
    l=1
    
    for row in rows:
        page_id = str(row[0])
        page_name = row[1]
        print page_id,page_name
        print k
        k=k+1
   

        base_url ='https://graph.facebook.com/v2.6/'+page_id+'/posts?limit=25&until=1401834693&__paging_token=enc_AdAeyYkjzX1tLJoB3x4JkoRtQ6qW9dd1jbDJZAadek3or8ZBvZARaSFCsjsxZBJsi5nqN6U4isMH3v5u3FOjAvC0QNw4P9mLnI2PaJxniTnDFFyVngZDZD&access_token=EAAHaG7wYo5ABACV5RR76FKwGGw5IZBa2FwW3Qo4YvKvXrwjzy5jeuXWaX7D2CxM7Ur4ogyDDlVRzfcw4wWuqMRPQ8Op29f5AanV15U2hm7Re6rdaMEOqf2nvDgbaOgbSq6YWWebBLQImGRz15PFkudmSqhqoZD'
        feed = json.loads(requests.get(base_url).text)
        i=0
        for j in range(0,100):
            print i
            i=i+1
            
        
            for item in feed['data']:
                print item['id']
                print item['created_time']
            for item in feed['data']:
                post_id = item['id']
                created_time=item['created_time']
                if 'message' in item:
                    
                    message=item['message']
                    print item['message']
                else:
                    message =''
                
                    
               
                print k
                sql_insert = "INSERT INTO Posts(page_id,post_id,created_time,message,post_num) values (%s,%s,%s,%s,%s)"
                cur.execute(sql_insert,(page_id,post_id,created_time,message,k))
                con.commit()
                print "Post inserted."
                k=k+1
          
            try:
                base_url = feed['paging']['next']
                feed = json.loads(requests.get(base_url).text)
            except Exception:
                
                print base_url
                print "next page"
                print page_id
                break



    con.commit()
    cur.close()
    con.close()

get_feed()

