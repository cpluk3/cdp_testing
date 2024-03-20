import json
import uuid
from datetime import datetime

def get_dummy_id():
    return uuid.uuid4().hex


def get_dummy_persona_tagging(n=100):
    dummy_tag = "DUMMY_PERSONA_TAGGING_{}"
    tags = []
    for i in range(0, n):
        tags.append(dummy_tag.format(i))
    return tags

def get_key_value_list(n=10):
    data = {}
    for i in range(0, 10):
        data[f"DUMMY_METRIC_TAGGING_{i}"] = 10000
    return data

#assume 100 tags at max per user
def get_dummy_record(cust_id):
    data = {}
    data['cust_id'] = cust_id
    data['persona'] = get_dummy_persona_tagging(100)
    data['subscription'] = get_key_value_list(n=20)
    data['communications'] = get_key_value_list(n=10)
    data['spending'] = get_key_value_list(n=10)
    data['date_id'] = datetime.now().strftime("%Y-%m-%d")
    data['timestamp'] = datetime.now().timestamp()
    return data

#print(json.dumps(get_dummy_record(get_dummy_id())))
#exit()


import redis

r = redis.StrictRedis(host="172.19.16.13", port=6379, password="qqgoup1L!")
#r.set("foo1", "123.0")
for i in range(1, 1000000):
    dummy_id = get_dummy_id()
    dummy_record = get_dummy_record(dummy_id)
    r.set(dummy_id, json.dumps(dummy_record))
    if i % 100000 == 0:
        print(f"record {i} inserted")
