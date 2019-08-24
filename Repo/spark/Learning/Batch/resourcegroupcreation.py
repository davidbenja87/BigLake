import os
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
import config

# subscription_id = os.environ.get(
#     'AZURE_SUBSCRIPTION_ID',
#     '974668b8-821d-4cc2-a84d-c81a7733f464') # your Azure Subscription Id
# credentials = ServicePrincipalCredentials(
#     client_id=os.environ['cad57932-c660-412c-9e77-154a3c327f94'],
#     secret=os.environ['D2i:v4w=QCkH@tUfM=QyKvRPEENhYW27'],
#     tenant=os.environ['c8fedfb4-d804-457b-9745-362581de2e4c']
# )
# subscription_id =  config.azurerba['subscriptionId']
# credentials = ServicePrincipalCredentials(
#     client_id= config.azurerba['client_id'],
#     secret= config.azurerba['client_secret'],
#     tenant= config.azurerba['tenant']
# )

subscription_id = 'f444d84a-049a-43b9-be3b-10be59713bc5'
credentials = ServicePrincipalCredentials(
    client_id= '914c772b-af21-4323-acfb-cc161fd223a5',
    secret= '-=6Q8-[SyteGB1Ab9[LQgmClmNQIk[MZ',
    tenant= '9274ee3f-9425-4109-a27f-9fb15c10675d'
)
client = ResourceManagementClient(credentials, subscription_id)
resource_group_params = {'location':'westus'}
client.resource_groups.create_or_update('azure-sample-group', resource_group_params)