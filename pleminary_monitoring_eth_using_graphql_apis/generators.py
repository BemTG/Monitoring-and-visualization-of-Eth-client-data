import main
import datasets
import api_queries
from elasticsearch import helpers
from elasticsearch_dsl import connections
import elasticsearch
from elasticsearch import Elasticsearch


#enumerate through the json df
def generator_eth_data(df):
    ##loop through each json row (really the df rows)
    ## and return the following bew json data 
    for c,line in enumerate(df):
        ### this is the josn format elk processes data
        yield{
            '_index': 'ethdata',
#             '_type':'_doc',
            ##use a show id as it is column with unique values (basically index)
#             '_id':line.get('id0', None),
            '_source':{
                'datetime':line.get('datetime'),
                
                'sc_count':line.get('sc_count'),
                'number_of_contracts':line.get('number_of_contracts'),                
                'median_gas_price':line.get('median_gas_price'),
                'tx_count':line.get('tx_count')
#                 'prop_slashing_count':line.get('prop_slashing_count'),
#                 'attester_slashing_count':line.get('attester_slashing_count')
            }
        }

#enumerate through the json df
def generator_beacon_data(df):
    ##loop through each json row (really the df rows)
    ## and return the following new json data 
    for c,line in enumerate(df):
        ### this is the josn format elk processes data
        yield{
            '_index': 'beacondata',
#             '_type':'_doc',
            ##use a show id as it is column with unique values (basically index)
#             '_id':line.get('id0', None),
            '_source':{
                'datetime':line.get('datetime'),
                
                'block_count':line.get('block_count'),
                'proposers':line.get('proposers'),                
                'deposit_count':line.get('deposit_count'),
                'deposit_ammount_eth':line.get('deposit_ammount'),
                'prop_slashing_count':line.get('prop_slashing_count'),
                'attester_slashing_count':line.get('attester_slashing_count')
            }
        }
#         raise StopIteration


def ingest_data_to_elk( df, gen_query, from_date, till_date):
    
#     gen= gen_query(df)
    
    
    df= df.to_dict('records')
 
    mycustom= gen_query(df)
    
    print(next(mycustom))
    
    ENDPOINT= '<ELK ENDPOINT>' 
    es= Elasticsearch(timeout=600, hosts=ENDPOINT)
    
    try:
        res = helpers.bulk(es, gen_query(df))
        print(res)
        print('Wowza, its Working')
    except Exception as e:
        print('whoa, something is off')
        pass
