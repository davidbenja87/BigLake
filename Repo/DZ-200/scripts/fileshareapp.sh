#!/bin/bash
az appservice plan create --name blob-exercise-plan --resource-group "DP-200" --sku FREE --location "southindia"
az webapp create --name "filesharebenja" --plan blob-exercise-plan --resource-group "DP-200"
CONNECTIONSTRING=$(az storage account show-connection-string --name "fileshareapp" --output tsv)
az webapp config appsettings set --name "filesharebenja" --resource-group "DP-200" --settings AzureStorageConfig:ConnectionString=$CONNECTIONSTRING AzureStorageConfig:FileContainerName=files