# ETH Monitor Recap Video

<div align="center">
    
[![YouTube](http://i.ytimg.com/vi/TluyfvBE200/hqdefault.jpg)](https://www.youtube.com/watch?v=TluyfvBE200)

</div>


# Monitoring and visualizing Eth client data

Previously, in May there was a 7-block reorg which took the community by surprise and made it challenging to distinguish whether it was a malicious attack or a client implementation issue. After some time, it was later noted that this was due to certain validators not simply upgrading their software (caused by the proposer boost fork upgrade). <br>
You can read about it <a href='https://barnabe.substack.com/p/pos-ethereum-reorg'>here </a> or more detail.<br>
In such occurrences, an Ethereum Network monitoring tool could be very useful to  detect and send alerts when there are issues or suspicious activity occuring in the network. 

The goal here is to catalyse the time required to detect system failures, attacks and provide a means to interact with the Eth client data for research & analysis purposes. In addition, by utilising ML models it would also be plausible to anticipate potential issues ahead of time and provide system health updates routinely.

As Eth scales it will be increasingly important to detect and respond to network issues and potential attacks rapidly, hence tracking and analysing client data as well as on-chain events could be beneficial to get a hollistic overview of how the various clients are behaving.

# Architecture

The eth client data will be monitored using the ELK stack (Elasticsearc, Logstash and Kibana) as it can scale very well with the increasing data.

<img src='https://daoagents.s3.amazonaws.com/Quick_ct/arc.png' width="50%" height="50%" style='display: block;    
    margin: 0 auto;'>
<img width="60%" height="60%" src='https://daoagents.s3.amazonaws.com/Quick_ct/pipeline.png' style='display: block;    
    margin: 0 auto;'>



