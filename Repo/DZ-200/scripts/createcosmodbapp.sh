#!/bin/bash


# set execution context (if necessary)
# az account set --subscription "974668b8-821d-4cc2-a84d-c81a7733f464"

# Set the resource group name and location for your server
resourceGroupName="learn-ca95e5f2-9d5c-4683-a4a6-435f1c4f713f"
# location=southindia

export NAME="cosmos1559"

# Set an admin login and password for your database

# password=<EnterYourComplexPasswordHere1>


# Create Cosmodb Account

az cosmosdb create \
	--name $NAME \
	--resource-group $resourceGroupName
# set environment variable for endpoint and keys

export ENDPOINT=$(az cosmosdb list --resource-group learn-ca95e5f2-9d5c-4683-a4a6-435f1c4f713f \
        --output tsv --query [0].documentEndpoint)

export KEY=$(az cosmosdb keys list --resource-group "learn-ca95e5f2-9d5c-4683-a4a6-435f1c4f713f" \
        --name $NAME --output tsv --query primaryMasterKey)		


	
# Create Cosmodb database

az cosmosdb database create \
		--name $NAME \
		--db-name "mslearn" \
		--resource-group $resourceGroupName

# # Create collection

az cosmosdb collection create \
	--name $NAME \
	--db-name "mslearn" \
	--collection-name "Small" \
	--partition-key-path "/id" \
	--throughput 400 \
	--resource-group $resourceGroupName

az cosmosdb collection create \
	--name $NAME \
	--db-name "mslearn" \
	--collection-name "HotPartition" \
	--partition-key-path "/Item/Category" \
	--throughput 7000 \
	--resource-group $resourceGroupName

az cosmosdb collection create \
	--name $NAME \
	--db-name "mslearn" \
	--collection-name "Orders" \
	--partition-key-path "/Item/Id" \
	--throughput 7000 \
	--resource-group $resourceGroupName


# # Zone redundancy is only supported in the premium and business critical service tiers

# # Echo random password
# echo $password

echo $ENDPOINT
echo $KEY