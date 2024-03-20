import redis

import json
import uuid
from datetime import datetime


r = redis.StrictRedis(host="172.19.16.13", port=6379, password="qqgoup1L!")
x = r.get("af70afff35464d44859a82f658ff5822")
print(x)
