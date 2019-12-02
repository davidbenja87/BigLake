#!/bin/bash
echo "Hello World"
RESOURCE_GROUP="DP-200"
STORAGE_NAME="fileshareapp"
az storage account create \
        --resource-group "DP-200" \
        --kind storageV2 \
        --sku Standard_LRS \
        --access-tier Cool \
        --name "fileshareapp"
echo "$STORAGE_NAME"