import pymysql
from time import sleep
import requests
import json
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

access_token = "EAAYUZByQgzIkBAAQwsYZCxXj9r33XSLz3kzE8w0E42eujH3LlsVevRFnpyjkyhYRGgyKhFg4mArox2HfYvobcLPYQo0efZB59tUGWbBnrCRe7vpPdXX71gP92QZAHUOZBxEBqzEqIGISdnCMTPWrbY2YggOvGcCkZD"
con = pymysql.connect(host='localhost',database='comic con india', user='root', charset='utf8')
cursor = con.cursor()
cursor.execute("SET sql_notes = 0;")
query= "CREATE TABLE IF NOT EXISTS `comicon_posts` (post_id varchar(100) NOT NULL PRIMARY KEY, created_time text, page_id varchar(100))"

#print query
cursor.execute(query)
con.commit()
query = "SELECT page_id FROM comicon_pages"
cursor.execute(query)
rows = cursor.fetchall()
i = 0
for row in rows:
	page_id=str(row[0])
	try:	
		base_url="https://graph.facebook.com/v2.6/"+page_id+"/posts?access_token="+access_token
		results = requests.get(base_url)
		results_text=results.text
		results_json=json.loads(results_text)
		print "check"
	except requests.exceptions.ConnectTimeout:
		print "sleep1"
		sleep(300)
	if len(results_json['data'])==0:
		print "skipped"+page_id 
	else:
		j=0
		for i in range(0,100):
			print j
			j=j+1
			for item in results_json['data']:
				
				post_id=item['id']
				if 'created_time' in item:
					created_time=item['created_time']
				
				#check="SELECT * FROM `postsnew` WHERE `post_id` LIKE '%s'" %(post_id) 
				#cursor.execute(check)
				#row=cursor.fetchall()
				#if len(row)==0:
					#continue		
				

				q="INSERT INTO `comicon_posts` (post_id,created_time,page_id) values('%s','%s','%s')" %(post_id,created_time,page_id)
				cursor.execute(q)
				con.commit()
				
			try:	
				base_url=results_json['paging']['next']
				results = requests.get(base_url)
				results_text=results.text
				results_json=json.loads(results_text)
			except KeyError:
				print base_url
				print "next page"
				print page_id
				print ++i
				print
				break
con.commit()
cursor.close()
con.close()




