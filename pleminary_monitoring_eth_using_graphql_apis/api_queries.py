

gas_q= {
       "query": "query ($network: EthereumNetwork!, $dateFormat: String!, $from: ISO8601DateTime, $till: ISO8601DateTime) {\n  ethereum(network: $network) {\n    transactions(options: {asc: \"date.date\"}, date: {since: $from, till: $till}) {\n      date: date {\n        date(format: $dateFormat)\n      }\n      gasPrice\n      gasValue\n      average: gasValue(calculate: average)\n      maxGasPrice: gasPrice(calculate: maximum)\n      medianGasPrice: gasPrice(calculate: median)\n    }\n  }\n}\n",
   "variables": "{\n  \"limit\": 10,\n  \"offset\": 0,\n  \"network\": \"ethereum\",\n  \"from\": \"2022-11-21\",\n  \"till\": \"2022-11-28T23:59:59\",\n  \"dateFormat\": \"%Y-%m-%d\"\n}"
    }

tx_count_q= {
       "query": "query ($network: EthereumNetwork!, $dateFormat: String!, $from: ISO8601DateTime, $till: ISO8601DateTime) {\n  ethereum(network: $network) {\n    transactions(options: {asc: \"date.date\"}, date: {since: $from, till: $till}) {\n      date: date {\n        date(format: $dateFormat)\n      }\n      count: countBigInt\n      gasValue\n    }\n  }\n}\n",
       "variables": "{\n  \"limit\": 10,\n  \"offset\": 0,\n  \"network\": \"ethereum\",\n  \"from\": \"2022-11-25T23:59:59\",\"till\":\"2022-11-28T23:59:59\",\n  \"dateFormat\": \"%Y-%m-%d\"\n}"
    }

smc_count_q= {
       "query": "query ($network: EthereumNetwork!, $dateFormat: String!, $from: ISO8601DateTime, $till: ISO8601DateTime) {\n  ethereum(network: $network) {\n    smartContractCalls(\n      options: {asc: \"date.date\"}\n      date: {since: $from, till: $till}\n    ) {\n      date: date {\n        date(format: $dateFormat)\n      }\n      count: countBigInt\n      contracts: countBigInt(uniq: smart_contracts)\n      callers: countBigInt(uniq: senders)\n      methods: countBigInt(uniq: smart_contract_methods)\n    }\n  }\n}\n",
       "variables": "{\n  \"limit\": 10,\n  \"offset\": 0,\n  \"network\": \"ethereum\",\n  \"from\": \"2022-11-25T23:59:59\",\"till\":\"2022-11-28T23:59:59\",\n  \"dateFormat\": \"%Y-%m-%d\"\n}"
    }

block_count_q= {
   "query": "\n            query ($network: Ethereum2Network!,\n                  $dateFormat: String!,\n\n                  $from: ISO8601DateTime,\n                  $till: ISO8601DateTime){\n                    ethereum2(network: $network ){\n                      blocks(options:{asc: \"date.date\"}, date: {\n                        since: $from\n                        till: $till}\n\n                      ) {\n                        date: date{\n                          date(format: $dateFormat)\n                        }\n                        count: countBigInt\n                        proposers: countBigInt(uniq: block_proposers)\n                      }\n                    }\n                  }",
   "variables": "{\"limit\":10,\"offset\":0,\"network\":\"eth2\",\"from\":\"2008-11-04\",\"till\":\"2022-11-22T23:59:59\",\"dateFormat\":\"%Y-%m-%d\"}"
     }

beacon_chain_deposits_q= {
   "query": "\n            query ($network: Ethereum2Network!,\n                  $dateFormat: String!,\n\n                  $from: ISO8601DateTime,\n                  $till: ISO8601DateTime){\n                    ethereum2(network: $network ){\n                      deposits(options:{asc: \"date.date\"}, date: {\n                        since: $from\n                        till: $till}\n\n                      ) {\n                        date: date{\n                          date(format: $dateFormat)\n                        }\n                        count: countBigInt\n                        amount\n                      }\n                    }\n                  }",
   "variables": "{\"limit\":10,\"offset\":0,\"network\":\"eth2\",\"from\":\"2008-11-04\",\"till\":\"2022-11-22T23:59:59\",\"dateFormat\":\"%Y-%m-%d\"}"
}

proposer_slashing_data_q= {
   "query": "query ($network: Ethereum2Network!, $dateFormat: String!, $from: ISO8601DateTime, $till: ISO8601DateTime) {\n  ethereum2(network: $network) {\n    proposerSlashings(\n      options: {asc: \"date.date\"}\n      date: {since: $from, till: $till}\n    ) {\n      date: date {\n        date(format: $dateFormat)\n      }\n      count: countBigInt\n      slashing_proposers: countBigInt(uniq: slashing_proposers)\n    }\n  }\n}\n",
   "variables": "{\n  \"limit\": 10,\n  \"offset\": 0,\n  \"network\": \"eth2\",\n  \"from\": \"2008-11-04\",\n  \"till\": \"2022-11-22T23:59:59\",\n  \"dateFormat\": \"%Y-%m-%d\"\n}"
}

attester_slashing_q= {
   "query": "\n            query ($network: Ethereum2Network!,\n                  $dateFormat: String!,\n\n                  $from: ISO8601DateTime,\n                  $till: ISO8601DateTime){\n                    ethereum2(network: $network ){\n                      attesterSlashings(options:{asc: \"date.date\"}, date: {\n                        since: $from\n                        till: $till}\n\n                      ) {\n                        date: date{\n                          date(format: $dateFormat)\n                        }\n                        count: countBigInt\n                        slashing_validators: countBigInt(uniq: validators)\n                      }\n                    }\n                  }",
   "variables": "{\"limit\":10,\"offset\":0,\"network\":\"eth2\",\"from\":\"2008-11-04\",\"till\":\"2022-11-22T23:59:59\",\"dateFormat\":\"%Y-%m-%d\"}"
}
