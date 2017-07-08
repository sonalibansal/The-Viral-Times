import requests
import json
import pymysql
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()


con = pymysql.connect(host='localhost',database='auto', user='root',charset='utf8')
cur = con.cursor()
sql="ALTER TABLE Pages_posts ADD Post_number bigint"
cur.execute(sql)
sql2="SELECT post_id FROM Pages_posts"
cur.execute(sql2)

for i in range(1,2719):
    print i
    sql1="UPDATE Pages_posts SET Post_number=%s WHERE post_id=%s"
    cur.execute(sql1,i,post_id)
    con.commit()

        
cur.close()
con.close()


