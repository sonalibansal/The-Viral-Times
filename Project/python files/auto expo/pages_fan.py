import requests
import json
import pymysql
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

access_token = 'EAAHaG7wYo5ABACV5RR76FKwGGw5IZBa2FwW3Qo4YvKvXrwjzy5jeuXWaX7D2CxM7Ur4ogyDDlVRzfcw4wWuqMRPQ8Op29f5AanV15U2hm7Re6rdaMEOqf2nvDgbaOgbSq6YWWebBLQImGRz15PFkudmSqhqoZD'

def get_fan_count():

    con = pymysql.connect(host='localhost',database='auto', user='root',charset='utf8mb4')
    cur = con.cursor()
    sql = "SELECT page_id,page_name FROM AutoExpo_pages"
    cur.execute(sql)
    rows = cur.fetchall()
    sql_create_table = "CREATE TABLE IF NOT EXISTS Pages_fan(page_id bigint unsigned,page_name varchar(250),fan_count bigint unsigned,people_talking_about bigint unsigned,checkins bigint unsigned)"
    cur.execute(sql_create_table)
    con.commit()
    print "Table created..."
    
    for row in rows:
        page_id = str(row[0])
        page_name = row[1]
        print page_id,page_name

   

        base_url ='https://graph.facebook.com/v2.6/'+page_id+'/?fields=fan_count,talking_about_count,checkins&access_token=EAAHaG7wYo5ABACV5RR76FKwGGw5IZBa2FwW3Qo4YvKvXrwjzy5jeuXWaX7D2CxM7Ur4ogyDDlVRzfcw4wWuqMRPQ8Op29f5AanV15U2hm7Re6rdaMEOqf2nvDgbaOgbSq6YWWebBLQImGRz15PFkudmSqhqoZD'
        feed = json.loads(requests.get(base_url).text)
        print feed['fan_count']
        print feed['talking_about_count']
        print feed['checkins']
        fan_count=feed['fan_count']
        people_talking_about=feed['talking_about_count']
        checkins=feed['checkins']

        sql_insert = "INSERT INTO Pages_fan (page_id,page_name,fan_count,people_talking_about,checkins) values (%s,%s,%s,%s,%s)"
        cur.execute(sql_insert,(page_id,page_name,fan_count,people_talking_about,checkins))
        con.commit()
        print "data inserted."
    
          
           
          



    cur.close()
    con.close()

get_fan_count()

