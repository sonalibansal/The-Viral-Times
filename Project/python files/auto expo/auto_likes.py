import requests
import json
import pymysql
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

access_token = 'EAAHaG7wYo5ABACR9rbHjURYuJrrYnn6ZCaxTsymrCcSIBvlOhgtVWE78RHekQKltGBPcvMqPEvUVi2eJGKnieDMrVGwRNpkFJP4t3F1VoobHkyI5nZAixWKnzz6xfmwimvbDDQyMEBqed2aQzV1Mj3wb0ZBV7gZD'

def get_feed():

    con = pymysql.connect(host='localhost',database='auto', user='root',charset='utf8mb4')
    cur = con.cursor()
    sql = " SELECT post_id,created_time,page_id FROM Posts"
    cur.execute(sql)
    rows = cur.fetchall()
    sql_create_table = "CREATE TABLE IF NOT EXISTS Likes (page_id bigint unsigned, post_id varchar(100) NOT NULL PRIMARY KEY,created_time timestamp,likes bigint unsigned)"
    cur.execute(sql_create_table)
    con.commit()
    print "Table created..."
    i=1
    
    for row in rows:
        print i
        i=i+1
        page_id = str(row[0])
        post_id = row[1]
        created_time= str(row[2])
        print page_id,post_id,created_time

        base_url='https://graph.facebook.com/v2.6/'+post_id+'/likes?pretty=0&summary=true&access_token='+access_token
        feed = json.loads(requests.get(base_url).text)
        if(len(feed['data'])==0):
             print "skipped"+post_id
        else:
            
            
             
            try:
                likes=feed['summary']['total_count']
                print likes

                sql_insert = "INSERT INTO Likes(page_id,post_id,created_time,likes) values (%s,%s,%s,%s)"
                cur.execute(sql_insert,(page_id,post_id,created_time,likes))
                con.commit()
                print "likes counted"
            except KeyEdrror:
                    print "error"+post_id


            
        
       
        
       
  
    
          



    cur.close()
    con.close()

get_feed()

