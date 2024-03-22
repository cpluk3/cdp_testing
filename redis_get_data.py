import time
import random
import redis
how_many_times = 10000
run_time_list = []
host = "172.19.16.8"
r = redis.StrictRedis(host = host, port=6379, password="qqgoup1L!" )
all_keys = r.keys()
for i in range(how_many_times):

    chosen_key = random.choice(all_keys)
    start_time = time.time()
    random_value = r.get(chosen_key)
    end_time = time.time()

    time_difference = end_time - start_time
    run_time_list.append(time_difference)

import statistics as stat
print("Mean: ", stat.mean(run_time_list))
print("Median: ", stat.median(run_time_list))
print("Max: ", max(run_time_list))
print("Min: ", min(run_time_list))
