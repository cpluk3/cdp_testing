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

print(client.list_database_names())

import time
start_time = time.time()
print("Current time in seconds333 since the epoch", start_time)
times = 1800000
for i in range(times):
    mycol.insert_one(dummy_data.get_dummy_record(str(dummy_data.get_dummy_id())))
    if i % 100000 == 0:
        print(f"record {i} inserted")
        sub_end = time.time()
        print("sub_end: ", sub_end - start_time)

end_time = time.time()
time_difference = end_time-start_time
print("Time difference: ", time_difference)
