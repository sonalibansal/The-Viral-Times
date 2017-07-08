import requests
import json
import pymysql

access_token = 'EAAHYJXZB5WPwBAPAZBpa8W0hlgOxvBFe24SzUczHihFadkdhP93obmlu99lfBMMCGlIBALOpQ2GXnnS6HXpjX9JaDUB5Dlny1eim2uPgX3cWafdZCe2ljBTiDTDPmKP4KxYEOZC4ZAFWL7Sm6oENUvEriZBe3x6OgZD'

def get_page(page_name):
    con = pymysql.connect(user='root',password ='', database = 'viral_db',charset='utf8')
    cur = con.cursor()
    sql_create_table = "CREATE TABLE IF NOT EXISTS facebook_Pages (page_id bigint unsigned NOT NULL PRIMARY KEY, page_name varchar(250), fan_count bigint unsigned, people_talking bigint unsigned, checked_in bigint unsigned)"
    cur.execute(sql_create_table)
    con.commit()
    base_url = 'https://graph.facebook.com/v2.6/search?limit=25&type=page&q='+page_name+'&access_token='+access_token
    print base_url
    results = requests.get(base_url)
    print results.text
    results_text = results.text
    results_json = json.loads(results_text)
    print results_json
    for item in results_json['data']:
        page_id = item['id']
        page_name = item['name']
        base_url = 'https://graph.facebook.com/v2.6/'+page_id+'?fields=fan_count,talking_about_count,checkins&access_token=EAAHYJXZB5WPwBAPAZBpa8W0hlgOxvBFe24SzUczHihFadkdhP93obmlu99lfBMMCGlIBALOpQ2GXnnS6HXpjX9JaDUB5Dlny1eim2uPgX3cWafdZCe2ljBTiDTDPmKP4KxYEOZC4ZAFWL7Sm6oENUvEriZBe3x6OgZD'
        likes = json.loads(requests.get(base_url).text)
        fan = likes['fan_count']
        talking_about = likes['talking_about_count']
        checked_in = likes['checkins']
        sql_insert = "INSERT INTO facebook_pages (page_id,page_name,fan_count,people_talking,checked_in) values('%s', '%s','%s','%s','%s')" % (item['id'],item['name'],fan,talking_about,checked_in)
        cur.execute(sql_insert)
        con.commit()
        print "record inserted"
    cur.close()
    con.close()
get_page('National Youth Festival')
