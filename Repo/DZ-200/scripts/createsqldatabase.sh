#!/bin/bash


# set execution context (if necessary)
az account set --subscription "974668b8-821d-4cc2-a84d-c81a7733f464"

# Set the resource group name and location for your server
resourceGroupName="DP-200"
location=southindia

databasename="logistics"

# Set an admin login and password for your database
adminlogin=ServerAdmin
password="@seek1234"
# password=<EnterYourComplexPasswordHere1>

# The logical server name has to be unique in the system
servername=server-benja

# The ip address range that you want to allow to access your DB
startip=92.18.78.183
endip=92.18.78.183

startipcli=40.118.110.145
endipcli=40.118.110.145

# Create a resource group
az group create \
    --name $resourceGroupName \
    --location $location

# Create a logical server in the resource group
az sql server create \
    --name $servername \
    --resource-group $resourceGroupName \
    --location $location  \
    --admin-user $adminlogin \
    --admin-password $password

# Configure a firewall rule for the server
az sql server firewall-rule create \
    --resource-group $resourceGroupName \
    --server $servername \
    -n AllowYourIp \
    --start-ip-address $startip \
    --end-ip-address $endip
	
# Configure a firewall rule for the server
az sql server firewall-rule create \
    --resource-group $resourceGroupName \
    --server $servername \
    -n AllowYourCli \
    --start-ip-address $startipcli \
    --end-ip-address $endipcli	

# Create a database in the server with zone redundancy as false
az sql db create \
    --resource-group $resourceGroupName \
    --server $servername \
    --name $databasename \
    --edition Free \
    --zone-redundant false

# Zone redundancy is only supported in the premium and business critical service tiers

# Echo random password
echo $password