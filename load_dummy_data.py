import json
import uuid
from datetime import datetime

def get_dummy_id():
    return uuid.uuid4()

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



print(get_dummy_record(get_dummy_id()))

#for i in range(0, 10):
#    print(get_dummy_id())

