

def eth_data( from_date, till_date):
  #gas cost data
  gas_cost= get_data(gas_q, from_date, till_date)
  gas_data=json.loads(gas_cost.decode("utf-8"))
  # print(gas_data)
  gas_price=[]

  for i in range(0,len(gas_data['data']['ethereum']['transactions'])):
    g_data=[]
    g_data.append(gas_data['data']['ethereum']['transactions'][i]['date']['date'])
    g_data.append(gas_data['data']['ethereum']['transactions'][i]['medianGasPrice'])
    g_data.append(gas_data['data']['ethereum']['transactions'][i]['maxGasPrice'])
    gas_price.append(g_data)


  # print(gas_price)
  df_gasprice= pd.DataFrame(gas_price)
  df_gasprice[0] = pd.to_datetime(df_gasprice[0])
  df_gasprice = df_gasprice.rename(columns={1: 'median_gas_price', 0:'datetime', 2:'maxGasPrice' })

  df_gasprice['datetime'] = pd.to_datetime(df_gasprice['datetime']).dt.tz_localize('Europe/London').dt.tz_convert('UTC')


  # tx_count
  tx_data= get_data(tx_count_q, from_date, till_date)
  tx_data=json.loads(tx_data.decode("utf-8"))

  tx_count=[]

  for i in range(0,len(tx_data['data']['ethereum']['transactions'])):
    t_data=[]
    t_data.append(tx_data['data']['ethereum']['transactions'][i]['date']['date'])
    t_data.append(tx_data['data']['ethereum']['transactions'][i]['count'])
    tx_count.append(t_data)

  df_tx= pd.DataFrame(tx_count)
  df_tx[0] = pd.to_datetime(df_tx[0])
  df_tx = df_tx.rename(columns={1: 'tx_count', 0:'datetime'})
  df_tx['datetime'] = pd.to_datetime(df_tx['datetime']).dt.tz_localize('Europe/London').dt.tz_convert('UTC')

  #smart contract
  smc_call= get_data(smc_count_q, from_date, till_date)
  smc_call=json.loads(smc_call.decode("utf-8"))

  smc_tot_calls=[]

  for i in range(0,len(smc_call['data']['ethereum']['smartContractCalls'])):
    smc_data=[]
    smc_data.append(smc_call['data']['ethereum']['smartContractCalls'][i]['date']['date'])
    smc_data.append(smc_call['data']['ethereum']['smartContractCalls'][i]['count'])
    smc_data.append(smc_call['data']['ethereum']['smartContractCalls'][i]['contracts'])
    smc_data.append(smc_call['data']['ethereum']['smartContractCalls'][i]['callers'])
    smc_tot_calls.append(smc_data)

  # print(smc_tot_calls)
  df_sc= pd.DataFrame(smc_tot_calls)
  df_sc[0] = pd.to_datetime(df_sc[0])
  df_sc = df_sc.rename(columns={1: 'sc_count', 0:'datetime', 2:'number_of_contracts', 3:'sc_callers'})
  df_sc['datetime'] = pd.to_datetime(df_sc['datetime']).dt.tz_localize('Europe/London').dt.tz_convert('UTC')
  # print(df_sc)

  #concat datasets
  df_conc= pd.merge(df_sc, df_gasprice, on='datetime')
  df_conc= pd.merge(df_conc, df_tx, on='datetime')

  merged_df= df_conc.iloc[:,1:]
  merged_df= merged_df.astype(float)
  merged_df['datetime']= df_conc['datetime']
    
  return merged_df


def beacon_chain_data( from_date, till_date):
  #block count
  block_info= get_data(block_count_q, from_date, till_date)
  block_info=json.loads(block_info.decode("utf-8"))
  # print(gas_data)
  block_count=[]

  for i in range(0,len(block_info['data']['ethereum2']['blocks'])):
    block_data=[]
    block_data.append(block_info['data']['ethereum2']['blocks'][i]['date']['date'])
    block_data.append(block_info['data']['ethereum2']['blocks'][i]['count'])
    block_data.append(block_info['data']['ethereum2']['blocks'][i]['proposers'])
    block_count.append(block_data)


  df_block= pd.DataFrame(block_count)
  df_block[0] = pd.to_datetime(df_block[0])
  df_block = df_block.rename(columns={1: 'block_count', 0:'datetime', 2:'proposers'})
  df_block['datetime'] = pd.to_datetime(df_block['datetime']).dt.tz_localize('Europe/London').dt.tz_convert('UTC')
  print(df_block)

  
  # deposit_info
  deposit_counts= get_data(beacon_chain_deposits_q, from_date, till_date)
  deposit_counts=json.loads(deposit_counts.decode("utf-8"))

  deposit_count_res=[]

  for i in range(0,len(deposit_counts['data']['ethereum2']['deposits'])):
    dep_data=[]
    dep_data.append(deposit_counts['data']['ethereum2']['deposits'][i]['date']['date'])
    dep_data.append(int(deposit_counts['data']['ethereum2']['deposits'][i]['count']))
    dep_data.append(deposit_counts['data']['ethereum2']['deposits'][i]['amount'])
    deposit_count_res.append(dep_data)
  
  if deposit_count_res:
    df_deposit_info= pd.DataFrame(deposit_count_res)
    df_deposit_info[0] = pd.to_datetime(df_deposit_info[0])
    df_deposit_info = df_deposit_info.rename(columns={1: 'deposit_count', 
                                0:'datetime', 2:'deposit_ammount'})
  else:
      blanks=[[from_date,0,0],[till_date,0,0]]
      df_deposit_info= pd.DataFrame(blanks)
      df_deposit_info[0] = pd.to_datetime(df_deposit_info[0])
      df_deposit_info = df_deposit_info.rename(columns={1: 'deposit_count', 
                                  0:'datetime', 2:'deposit_ammount'})
      df_deposit_info=df_deposit_info.head(1)

  df_deposit_info['datetime'] = pd.to_datetime(df_deposit_info['datetime']).dt.tz_localize('Europe/London').dt.tz_convert('UTC')
  print(df_deposit_info)
  
  
  #proposer slashing
  proposer_info= get_data(proposer_slashing_data_q, from_date, till_date)
  proposer_info=json.loads(proposer_info.decode("utf-8"))

  prop_slash=[]

  for i in range(0,len(proposer_info['data']['ethereum2']['proposerSlashings'])):
    prop_slash_data=[]
    prop_slash_data.append(proposer_info['data']['ethereum2']['proposerSlashings'][i]['date']['date'])
    prop_slash_data.append(int(proposer_info['data']['ethereum2']['proposerSlashings'][i]['count']))
    prop_slash_data.append(proposer_info['data']['ethereum2']['proposerSlashings'][i]['slashing_proposers'])
    prop_slash.append(prop_slash_data)

  # print(smc_tot_calls)
  if prop_slash:
    df_prop_slash= pd.DataFrame(prop_slash)
    df_prop_slash[0] = pd.to_datetime(df_prop_slash[0])
    df_prop_slash = df_prop_slash.rename(columns={1: 'prop_slashing_count', 
                                    0:'datetime', 2:'slashing_proposers'})
  else:
    blanks=[[from_date,0,0],[till_date,0]]
    df_prop_slash= pd.DataFrame(blanks)
    df_prop_slash[0] = pd.to_datetime(df_prop_slash[0])
    df_prop_slash = df_prop_slash.rename(columns={1: 'prop_slashing_count', 
                                    0:'datetime', 2:'slashing_proposers'})
    df_prop_slash=df_prop_slash.head(1)
      
  df_prop_slash['datetime'] = pd.to_datetime(df_prop_slash['datetime']).dt.tz_localize('Europe/London').dt.tz_convert('UTC')
  print(df_prop_slash)
  
  
  
  #attester slashing
  attester_info= get_data(attester_slashing_q, from_date, till_date)
  attester_info=json.loads(attester_info.decode("utf-8"))

  att_slash=[]

  for i in range(0,len(attester_info['data']['ethereum2']['attesterSlashings'])):
    att_slash_data=[]
    att_slash_data.append(attester_info['data']['ethereum2']['attesterSlashings'][i]['date']['date'])
    att_slash_data.append(int(attester_info['data']['ethereum2']['attesterSlashings'][i]['count']))
    att_slash_data.append(attester_info['data']['ethereum2']['attesterSlashings'][i]['slashing_validators'])
    att_slash.append(att_slash_data)

  # print(smc_tot_calls)
  if att_slash:
    df_att_slash= pd.DataFrame(att_slash)
    df_att_slash[0] = pd.to_datetime(df_att_slash[0])
    df_att_slash = df_att_slash.rename(columns={1: 'attester_slashing_count', 
                                    0:'datetime', 2:'slashing_attester'}) 
  else:

    blanks=[[from_date,0,0],[till_date,0,0]]
    df_att_slash= pd.DataFrame(blanks)
    df_att_slash[0] = pd.to_datetime(df_att_slash[0])
    df_att_slash = df_att_slash.rename(columns={1: 'attester_slashing_count', 
                                    0:'datetime', 2:'slashing_attester'})
    df_att_slash=df_att_slash.head(1)

  df_att_slash['datetime'] = pd.to_datetime(df_att_slash['datetime']).dt.tz_localize('Europe/London').dt.tz_convert('UTC')
  print(df_att_slash)
  

  #concat datasets
  df_conc2= pd.merge(df_block, df_deposit_info, on='datetime')
#     df_conc2= pd.merge(df_conc2, df_tx, on='datetime')
  df_conc2= df_conc2.merge(df_prop_slash,how='left', left_on='datetime', right_on='datetime')
  df_conc2= df_conc2.merge(df_att_slash,how='left', left_on='datetime', right_on='datetime')
  df_beacon= df_conc2.fillna(0)

  beacon_merged_df= df_beacon.iloc[:,1:]
  beacon_merged_df= beacon_merged_df.astype(float)
  beacon_merged_df['datetime']= df_beacon['datetime']
  
  return beacon_merged_df
