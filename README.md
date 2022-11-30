# Monitoring and visualizing Eth client data

Previously, in May there was a 7-block reorg which took the community by surprise and made it challenging to distinguish whether it was a malicious attack or a client implementation issue. After some time, it was later noted that this was due to certain validators not simply upgrading their software (caused by the proposer boost fork upgrade). You can read about it <a href='https://barnabe.substack.com/p/pos-ethereum-reorg'>here </a>. In such occurrences, an Ethereum Network monitoring tool could be very useful to  detect and send alerts when there are issues or suspicious activity occuring in the network. 

The goal here is to catalyse the time required to address system failures, attacks and provide a means to interact with the Eth client data for research & analysis purposes. In addition, by utilising ML models it would also be possible to anticipate potential issues ahead of time and provide system health updates when there happens to be unusual activity occurring in the network.

A monitoring system to track and analyse client data as well as on-chain events could be beneficial to get a hollistic overview of how the system is behaving. Morover, as Eth scales it will be increasingly important to detect and respond to network issues and potential attacks rapidly.

# Architecture

The eth client will be monitored using the ELK stack (Elasticsearc, Logstash and Kibana) as it can scale with the increasing data very well and being really fast.

<img src='https://daoagents.s3.amazonaws.com/Quick_ct/arc.png' width="60%" 
     height="60%">
<img src='https://daoagents.s3.amazonaws.com/Quick_ct/arc.png' width="60%" 
     height="60%" >
