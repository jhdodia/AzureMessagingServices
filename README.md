# AzureMessagingServices using python
A sample of azure service bus to use cloud messaging transfermation.

# Service Bus Introductory
Microsoft Azure Service Bus is a reliable information delivery service. The purpose of this service is to make communication easier. When two or more parties want to exchange information, they need a communication facilitator. Service Bus is a brokered, or third-party communication mechanism.

Different situations call for different styles of communication. Sometimes, letting applications send and receive messages through a simple queue is the best solution. In other situations, an ordinary queue isn't enough; a queue with a publish-and-subscribe mechanism is better. In some cases, all that's needed is a connection between applications, and queues are not required. Azure Service Bus provides all three options, enabling your applications to interact in several different ways.

Service Bus is a multi-tenant cloud service, which means that the service is shared by multiple users. Each user, such as an application developer, creates a namespace, then defines the communication mechanisms needed within that namespace. Figure 1 shows this architecture:

for more details follow: https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-fundamentals-hybrid-solutions

# Required Things to use this sample
##### *From Azure Portal:*
- **Azure Account:** To user azure cloud services (You can open free account for trial. Use This link to open free Accout: https://azure.microsoft.com/en-in/free/).
- **Resource Group:** The resource group stores metadata about the resources. Therefore, when you specify a location for the resource group, you are specifying where that metadata is stored. For compliance reasons, you may need to ensure that your data is stored in a particular region. (How To Create Resource refer: https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-portal)
- 
