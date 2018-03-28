
# AzureMessagingServices using python
Cloud Messaging Transformation with Azure Service Bus using Python.

# Service Bus Introductory
Microsoft Azure Service Bus is a reliable information delivery service. The purpose of this service is to make communication easier. When two or more parties want to exchange information, they need a communication facilitator. Service Bus is a brokered, or third-party communication mechanism.

Different situations call for different styles of communication. Sometimes, letting applications send and receive messages through a simple queue is the best solution. In other situations, an ordinary queue isn't enough; a queue with a publish-and-subscribe mechanism is better. In some cases, all that's needed is a connection between applications, and queues are not required. Azure Service Bus provides all three options, enabling your applications to interact in several different ways.

Service Bus is a multi-tenant cloud service, which means that the service is shared by multiple users. Each user, such as an application developer, creates a namespace, then defines the communication mechanisms needed within that namespace. Figure 1 shows this architecture:

for more details follow: https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-fundamentals-hybrid-solutions

# Required Things to use this sample
##### *From Azure Portal:*
- **Azure Account:** To user azure cloud services (You can open free account for trial. Use This link to open free Account: https://azure.microsoft.com/en-in/free/).
- **Resource Group:** The resource group stores metadata about the resources. Therefore, when you specify a location for the resource group, you are specifying where that metadata is stored. For compliance reasons, you may need to ensure that your data is stored in a particular region. (How To Create Resource refer: https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-portal)
- **Service Bus, Namespace, Shared Access Key and Shared Access Value:** 
  - **Namesapce:**
Windows Azure Service Bus is a brokered, scalable, multi-featured messaging queuing system. It's a reliable message queuing and durable publish/subscribe system. To begin using Service Bus messaging entities in Azure, you must first create a namespace with a name that is unique across Azure. A namespace provides a scoping container for addressing Service Bus resources within your application.
  - **Shared Access Key & Value:** Creating a new namespace automatically generates an initial Shared Access Signature (SAS) rule with an associated pair of primary and secondary keys that each grant full control over all aspects of the namespace. Basically used to gain access to Azure Service Bus resources using Shared Access Signature (SAS) token authentication. (How to Create Name Space, Shared Access Key and Value refer: https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-dotnet-how-to-use-topics-subscriptions).
    - In config.json file we need to set following things to access services bus resources.
    ```
    {
        "ServiceBusService":{
            "service_namespace":"",                                 // Apply Create Service Bus Name
            "shared_access_key_name":"RootManageSharedAccessKey",
            "shared_access_key_value":""                            // Apply Primary Key show after click on 'RootManageSharedAccessKey'
        }
    }
    ```


##### *From Python:*
- **Installed Python**
- **Install Azure Python package:** Refer https://pypi.python.org/pypi/azure

# Code Overview
#### servibusAgentSimulator Python File
This  File contains all terminology to send and receive messages using azure service bus.
#### *Short brief to use services bus messaging*
- Import Azure Services Bus Packages
```
from azure.servicebus import ServiceBusService, Message, Topic, Rule, DEFAULT_RULE_NAME
import json
```
- Create Service Bus Instance using Shared Access Credentials
```
with open('config.json') as json_data_file:
    config_dict = json.load(json_data_file)
	
bus_service = ServiceBusService(
    service_namespace=config_dict['ServiceBusService']['service_namespace'],
    shared_access_key_name=config_dict['ServiceBusService']['shared_access_key_name'],
    shared_access_key_value=config_dict['ServiceBusService']['shared_access_key_value'])
```
 - Create Topic Using Created Service Bus Instance
```
bus_service.create_topic('FieldGatway2AzureCloud')
```
 - Create Subscriptions
```
'''
Create subscriptions
-------------------------------------------------------------------------------------------
Subscriptions to topics are also created with the ServiceBusService object. 
Subscriptions are named and can have an optional filter that restricts the 
set of messages delivered to the subscription's virtual queue.

The MatchAll filter is the default filter that is used if no filter is specified 
when a new subscription is created. When the MatchAll filter is used, all messages 
published to the topic are placed in the subscription's virtual queue. The following 
example creates a subscription named AllMessages and uses the default MatchAll filter.
'''
bus_service.create_subscription('FieldGatway2AzureCloud', 'AllMessages')

'''
The following example creates a subscription named HighMessages with a SqlFilter 
that only selects messages that have a custom messagenumber property greater than 3:
'''
bus_service.create_subscription('FieldGatway2AzureCloud', 'HighMessages')
```
 - Send Message To a Topic
```
'''
Send messages to a topic
--------------------------------------------------------------------------------------------
To send a message to a Service Bus topic, your application must use the 
send_topic_message method of the ServiceBusService object.

The following example demonstrates how to send five test messages to mytopic. 
Note that the messagenumber property value of each message 
varies on the iteration of the loop (this determines which subscriptions receive it):
'''
for i in range(5):
    msg = Message('Msg {0}'.format(i).encode('utf-8'), custom_properties={'messagenumber':i})
    bus_service.send_topic_message('FieldGatway2AzureCloud', msg)
```
 - Receive Message from created topic
```
'''
Send messages to a topic
--------------------------------------------------------------------------------------------
To send a message to a Service Bus topic, your application must use the 
send_topic_message method of the ServiceBusService object.

The following example demonstrates how to send five test messages to mytopic. 
Note that the messagenumber property value of each message 
varies on the iteration of the loop (this determines which subscriptions receive it):
'''
for i in range(5):
    msg = Message('Msg {0}'.format(i).encode('utf-8'), custom_properties={'messagenumber':i})
    bus_service.send_topic_message('FieldGatway2AzureCloud', msg)
```
# Overall Explanation
In servibusAgentSimulator.py file i have describe main part of Service Bus Messaging in Code Overview area. 
- Topic Options
With relavant topic we can set the rules or option while creating topic. The create_topic method also supports additional options, which enable you to override default topic settings such as message time to live or maximum topic size. The following example sets the maximum topic size to 5 GB, and a time to live (TTL) value of 1 minute:
```
#topic_options = Topic()
#topic_options.max_size_in_megabytes = '5120'
#topic_options.default_message_time_to_live = 'PT1M'

#bus_service.create_topic('FieldGatway2AzureCloud', topic_options)
```
- Optional filter and virtual Ques of Subscriptions
Subscriptions are named and can have an optional filter that restricts the set of messages delivered to the subscription's virtual queue.

The MatchAll filter is the default filter that is used if no filter is specified when a new subscription is created. When the MatchAll filter is used, all messages published to the topic are placed in the subscription's virtual queue. The following example creates a subscription named AllMessages and uses the default MatchAll filter.
```
bus_service.create_subscription('FieldGatway2AzureCloud', 'AllMessages')
```
The following example creates a subscription named HighMessages with a SqlFilter that only selects messages that have a custom messagenumber property greater than 3:
```
bus_service.create_subscription('FieldGatway2AzureCloud', 'HighMessages')

rule = Rule()
rule.filter_type = 'SqlFilter'
rule.filter_expression = 'messagenumber > 3'

bus_service.create_rule('FieldGatway2AzureCloud', 'HighMessages', 'HighMessageFilter', rule)
bus_service.delete_rule('FieldGatway2AzureCloud', 'HighMessages', DEFAULT_RULE_NAME)
```

I have create tow message receivers and one sender of messages. Try to Execute First Agent, receivers, and senders in sequence and see observe the each window. Messages sends and receives happens using Azure Service Bus.
