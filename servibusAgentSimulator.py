from azure.servicebus import ServiceBusService, Message, Topic, Rule, DEFAULT_RULE_NAME
import json

with open('config.json') as json_data_file:
    config_dict = json.load(json_data_file)
	
'''
Create a topic
-------------------------------------------------------------------------------------------
The following code creates a ServiceBusService object. 
Replace mynamespace, sharedaccesskeyname, and sharedaccesskey with your actual 
namespace, Shared Access Signature (SAS) key name, and key value.
'''
bus_service = ServiceBusService(
    service_namespace=config_dict['ServiceBusService']['service_namespace'],
    shared_access_key_name=config_dict['ServiceBusService']['shared_access_key_name'],
    shared_access_key_value=config_dict['ServiceBusService']['shared_access_key_value'])
	
bus_service.create_topic('FieldGatway2AzureCloud')

'''
The create_topic method also supports additional options, 
which enable you to override default topic settings such as 
message time to live or maximum topic size. The following 
example sets the maximum topic size to 5 GB, and a time to live (TTL) value of 1 minute:
'''
#topic_options = Topic()
#topic_options.max_size_in_megabytes = '5120'
#topic_options.default_message_time_to_live = 'PT1M'

#bus_service.create_topic('FieldGatway2AzureCloud', topic_options)

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

rule = Rule()
rule.filter_type = 'SqlFilter'
rule.filter_expression = 'messagenumber > 3'

bus_service.create_rule('FieldGatway2AzureCloud', 'HighMessages', 'HighMessageFilter', rule)
bus_service.delete_rule('FieldGatway2AzureCloud', 'HighMessages', DEFAULT_RULE_NAME)

'''
Similarly, the following example creates a subscription named LowMessages with 
a SqlFilter that only selects messages that have a messagenumber property less than or equal to 3:
'''
bus_service.create_subscription('FieldGatway2AzureCloud', 'LowMessages')

rule = Rule()
rule.filter_type = 'SqlFilter'
rule.filter_expression = 'messagenumber <= 3'

bus_service.create_rule('FieldGatway2AzureCloud', 'LowMessages', 'LowMessageFilter', rule)
bus_service.delete_rule('FieldGatway2AzureCloud', 'LowMessages', DEFAULT_RULE_NAME)

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
	
'''
Receive messages from a subscription
--------------------------------------------------------------------------------------------
Messages are received from a subscription using the receive_subscription_message 
method on the ServiceBusService object:
'''
msg = bus_service.receive_subscription_message('FieldGatway2AzureCloud', 'LowMessages', peek_lock=False)
print(msg.body)