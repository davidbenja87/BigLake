import os
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient

subscription_id = os.environ.get(
    'AZURE_SUBSCRIPTION_ID',
    '974668b8-821d-4cc2-a84d-c81a7733f464') # your Azure Subscription Id
# credentials = ServicePrincipalCredentials(
#     client_id=os.environ['cad57932-c660-412c-9e77-154a3c327f94'],
#     secret=os.environ['D2i:v4w=QCkH@tUfM=QyKvRPEENhYW27'],
#     tenant=os.environ['c8fedfb4-d804-457b-9745-362581de2e4c']
# )

credentials = ServicePrincipalCredentials(
    client_id='cad57932-c660-412c-9e77-154a3c327f94',
    secret='D2i:v4w=QCkH@tUfM=QyKvRPEENhYW27',
    tenant='c8fedfb4-d804-457b-9745-362581de2e4c'
)
client = ResourceManagementClient(credentials, subscription_id)
resource_group_params = {'location':'westus'}
client.resource_groups.create_or_update('azure-sample-group', resource_group_params)