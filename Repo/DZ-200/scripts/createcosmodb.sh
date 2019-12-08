#!/bin/bash


# set execution context (if necessary)
az account set --subscription "974668b8-821d-4cc2-a84d-c81a7733f464"

# Set the resource group name and location for your server
resourceGroupName="DP-200"
location=southindia

export NAME=cosmos$RANDOM

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

# Create Cosmodb Account

az cosmosdb create \
	--name $NAME \
	--kind GlobalDocumentDB \
	--resource-group $resourceGroupName
	
# Create Cosmodb database

az cosmosdb database create \
		--name $NAME \
		--db-name "Products" \
		--resource-group $resourceGroupName

# Create collection

az cosmosdb collection create \
	--name $NAME \
	--db-name "Products" \
	--collection-name "Clothing" \
	--partition-key-path "/productId" \
	--throughput 400 \
	--resource-group $resourceGroupName
		
# Zone redundancy is only supported in the premium and business critical service tiers

# Echo random password
echo $password