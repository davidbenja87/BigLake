#!/bin/bash
echo "Hello World"
RESOURCE_GROUP="learn-88e67ece-28ac-4130-b7a2-01f49021e698"
STORAGE_NAME="fileshareapp"
az storage account create \
        --resource-group $RESOURCE_GROUP \
        --kind storageV2 \
        --sku Standard_LRS \
        --access-tier Hot \
        --name "fileshareapp"
echo "$STORAGE_NAME"
