#!/bin/bash
echo "Hello World"
RESOURCE_GROUP="DP-200"
STORAGE_NAME="bdaptestaccount2"
az storage account create \
        --resource-group "${RESOURCE_GROUP}" \
        --kind storageV2 \
        --sku Standard_LRS \
        --access-tier Cool \
        --name "${STORAGE_NAME}"
echo "$STORAGE_NAME"