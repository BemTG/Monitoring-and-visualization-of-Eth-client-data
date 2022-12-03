import http.client
import json
from datetime import timedelta, datetime
import pandas as pd
import os
import sys
import elasticsearch
from elasticsearch import Elasticsearch
import pandas as pd
import numpy as np
from elasticsearch import helpers
from elasticsearch_dsl import connections
import time
import schedule

import datasets
import api_queries
import generators




today= datetime.today().strftime('%Y-%m-%d')
yesterday= datetime.today() - timedelta(1)
yesterday= yesterday.strftime('%Y-%m-%d')
tommorow= datetime.today() + timedelta(1)
tommorow= tommorow.strftime('%Y-%m-%d')




def get_data(query,from_date, till_date):
    
    conn = http.client.HTTPSConnection("graphql.bitquery.io")
    payload = query
    
    var = json.loads(payload['variables'])
    var['from'] = var['from'].replace(var['from'] ,from_date)
    var['till'] = var['till'].replace(var['till'] ,till_date)
    payload['variables'] = json.dumps(var)
#     print(json.dumps(payload))
    payload=json.dumps(payload)

    headers = {
       'Content-Type': 'application/json',
       'X-API-KEY': '<API KEY>'
    }
    conn.request("POST", "/", payload, headers)
    res = conn.getresponse()
    res_data = res.read()
    # print(data.decode("utf-8"))
    return res_data




def ready_data_to_publish(t):
    print( "I'm working...", t)

    beacon_df= datasets.beacon_chain_data(today, today)
    eth_df= datasets.eth_data(today, today)
    print(beacon_df)
    print(eth_df)

    beacon_gen= generators.generator_beacon_data
    eth_gen=  generators.generator_eth_data

    generators.ingest_data_to_elk(beacon_df, beacon_gen ,  today, today)
    generators.ingest_data_to_elk(eth_df, eth_gen,  today, today)

    return



if __name__ == '__main__':

    schedule.every().day.at("23:59:59").do(ready_data_to_publish,'published data to elk')
    while True:
        print('waiting')
        schedule.run_pending()
        time.sleep(3) # wa



    
