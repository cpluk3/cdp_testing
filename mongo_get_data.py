from pymongo import MongoClient
import dummy_data

hostname= '172.19.16.6'
port = 27017
username = "mongouser"
password = "loveisgood@2024"

client = MongoClient(hostname, port, username=username, password=password)
print(client.database_name)
mydb = client["mydatabase"]
mycol = mydb["dummy_cust_info_180"]

import time
import random
how_many_times = 10000
run_time_list = []
for i in range(how_many_times):
    start_time = time.time()
    random_value = mydb.dummy_cust_info_180.find_one()
    end_time = time.time()

    run_time_list.append(end_time - start_time)

print(len(run_time_list))

import statistics as stat
number = stat.mean(run_time_list)
print(number)
print(max(run_time_list))
print(min(run_time_list))

