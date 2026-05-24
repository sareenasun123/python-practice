import requests
import mysql.connector
import json

url = "https://www.onlinekhabar.com/smtm/home/sector-performance"
viber_key = "569679cabdb02606-ec208a3f41b2b49b-852d389a8523312e"
user_id = "7Z0/kei3IcfquQS/wRXjUQ=="

db = mysql.connector.connect(
    user = "root",
    host = "localhost",
    database = "nepse"
)
terminal = db.cursor()
viber_url = "https://chatapi.viber.com/pa/post"

def store_into_database(data_dict):
    query = f"Insert into sector_performance (indices, turnover, percentage_change, points_change, advancers, decliners, latest_point, direction) values ('{data_dict['indices']}',{data_dict['turnover']},{ data_dict['percentage_change']}, {data_dict['points_change']}, {data_dict['advancers']}, {data_dict['decliners']}, {data_dict['latest_point']}, '{data_dict['direction']}')"



def send_message_to_viber(data):
    text = (
    f"The {data['indices']} index increased by "
    f"{data['points_change']} points ({data['percentage_change']}%) "
    f"and reached {data['latest_point']}. "
    f"A total turnover of {data['turnover']} was recorded, "
    f"with {data['advancers']} companies advancing and "
    f"{data['decliners']} declining."
)
    payload = {
        "auth_token":viber_key,
        "from": user_id, 
        "type":"text", 
        "text": text 
    }
    
    viber = requests.post(url=viber_url, data=json.dumps(payload))
    print(viber.json())


def fetch_sector():
    r = requests.get(url=url)
    if r.status_code == 200:
        for i in r.json()["response"]:
            print(i)
            send_message_to_viber(i)
            # store_into_database(i)
            
fetch_sector()
