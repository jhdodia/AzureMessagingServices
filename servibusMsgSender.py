from datetime import datetime, date, time
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


from uuid import getnode as get_mac
mac = raw_input("Mac: ")
payload = {"macid": mac,"timestamp":datetime.now().strftime("%b %d %Y %H:%M:%S")}
msg = Message(payload)
print payload
bus_service.send_topic_message('FieldGatway2AzureCloud',msg)
