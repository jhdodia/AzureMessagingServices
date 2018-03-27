
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

while True:	
	msg = bus_service.receive_subscription_message('FieldGatway2AzureCloud', 'AllMessages', timeout=1,peek_lock=False)		
	print(msg.body)
	