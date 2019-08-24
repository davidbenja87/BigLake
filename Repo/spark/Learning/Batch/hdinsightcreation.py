import os
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.hdinsight import HDInsightManagementClient
from azure.mgmt.hdinsight.models import *
import config



SUBSCRIPTION_ID =  config.azurerba['subscriptionId']

credentials = ServicePrincipalCredentials(
    client_id=config.azurerba['client_id'],
    secret=config.azurerba['client_secret'],
    tenant=config.azurerba['tenant']
)

client = HDInsightManagementClient(credentials, SUBSCRIPTION_ID)
# The name for the cluster you are creating
cluster_name = "biglakehdinsightauto"
# The name of your existing Resource Group
resource_group_name = "bdap-poc-playground"
# Choose a username
username = config.azure['username']
# Choose a password
password = config.azure['password']
# Replace <> with the name of your storage account
storage_account = "biglakestorageccountgen2.dfs.core.windows.net"
# biglakestorageaccount.dfs.core.windows.net
# Storage account key you obtained above
storage_account_key = config.azurerba['storage_account_key']
# Choose a region
location = "West Europe"
container = "biglake"

params = ClusterCreateProperties(
    cluster_version="3.6",
    os_type=OSType.linux,
    tier=Tier.standard,
    cluster_definition=ClusterDefinition(
        kind="spark",
        configurations={
            "gateway": {
                "restAuthCredential.enabled_credential": "True",
                "restAuthCredential.username": username,
                "restAuthCredential.password": password
            }
        }
    ),
    compute_profile=ComputeProfile(
        roles=[
            Role(
                name="headnode",
                target_instance_count=2,
                hardware_profile=HardwareProfile(vm_size="Large"),
                os_profile=OsProfile(
                    linux_operating_system_profile=LinuxOperatingSystemProfile(
                        username=username,
                        password=password
                    )
                )
            ),
            Role(
                name="workernode",
                target_instance_count=1,
                hardware_profile=HardwareProfile(vm_size="Large"),
                os_profile=OsProfile(
                    linux_operating_system_profile=LinuxOperatingSystemProfile(
                        username=username,
                        password=password
                    )
                )
            )
        ]
    )
    ,
    storage_profile=StorageProfile(
        storageaccounts=[StorageAccount(
            name=storage_account,
            key=storage_account_key,
            # container=container,
            file_system='bdap',
            # resource_id='/subscriptions/974668b8-821d-4cc2-a84d-c81a7733f464/resourceGroups/exampleplayground',
            # msi_resource_id='/subscriptions/974668b8-821d-4cc2-a84d-c81a7733f464/resourceGroups/exampleplayground/providers/Microsoft.ManagedIdentity/userAssignedIdentities/MangagedIdentity',
            is_default=True
        )]
    )
)

# create a hadoop cluster created with blob storage
client.clusters.create(
    cluster_name=cluster_name,
    resource_group_name=resource_group_name,
    parameters=ClusterCreateParametersExtended(
        location=location,
        tags={},
        properties=params
    ))

# destroy a hadoop cluster    

# client.clusters.delete(resource_group_name, cluster_name)