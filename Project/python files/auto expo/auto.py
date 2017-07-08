import requests
import json
import pymysql
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

access_token = 'EAAHaG7wYo5ABACV5RR76FKwGGw5IZBa2FwW3Qo4YvKvXrwjzy5jeuXWaX7D2CxM7Ur4ogyDDlVRzfcw4wWuqMRPQ8Op29f5AanV15U2hm7Re6rdaMEOqf2nvDgbaOgbSq6YWWebBLQImGRz15PFkudmSqhqoZD'

def search(page_name):
    
    base_url = 'https://graph.facebook.com/v2.6/search?pretty=0&q='+page_name+'&type=page&limit=25after=MjQZD&access_token=EAAHaG7wYo5ABAFXObEJoRUr3Mf7bQYK5g94qLRLZAwp6wGZBbAXIvjqMvV3RIyvTu8X9vgy8vTChZBD8V3OF5F1Phzjvqh5q1xNUsxtlh562PLtmyPOmkMjwXND9qLUcRhjdGpVnkpXHCNY9ahHWK0dy5zXCvIZD'
    results = requests.get(base_url)
    results_text = results.text
    results_json = json.loads(results_text)
    sql_create_table = "CREATE TABLE IF NOT EXISTS AutoExpo_pages(page_id bigint unsigned NOT NULL PRIMARY KEY, page_name varchar(250))"

    con = pymysql.connect(host='localhost',database='auto', user='root', charset='utf8')
    cur = con.cursor()
    cur.execute(sql_create_table)
    data=cur.fetchone()
    print "database version :%s "% data

    con.commit()

    for j in range(0,2):
        

        for item in results_json['data']:
            
            print item['name']
            print item['id']
            
            print ''

            page_id = item['id']
            page_name = item['name']
            sql_insert = "INSERT INTO AutoExpo_pages(page_id,page_name) values('"+page_id+"','"+page_name+"')"
            cur.execute(sql_insert)
            con.commit()
            print "Record inserted."
        try:
            base_url = results_json['paging']['next']   
            results=requests.get(base_url)  
            results_text=results.text
            results_json=json.loads(results_text)
        except:
            print "error"
        



    cur.close()
    con.close()

search('Auto Expo')

