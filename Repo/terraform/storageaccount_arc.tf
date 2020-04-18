# # resource "azurerm_resource_group" "test" {
# #   name     = "acctestRG-01"
# #   location = "West US"
# # }

# resource "azurerm_template_deployment" "example" {
#   name                = "acctesttemplate-01"
#   resource_group_name = "${azurerm_resource_group.example.name}"

#   template_body = <<DEPLOY
# {
#   "$schema": "https://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#",
#   "contentVersion": "1.0.0.0",
#   "parameters": {
#     "storageAccountType": {
#       "type": "string",
#       "defaultValue": "Standard_GRS",
#       "allowedValues": [
#         "Standard_LRS",
#         "Standard_GRS",
#         "Standard_ZRS"
#       ],
#       "metadata": {
#         "description": "Storage Account type"
#       }
#     }
#   },
#   "variables": {
#     "location": "[resourceGroup().location]",
#     "storageAccountName":  "${var.storageaccountname}",
#     "publicIPAddressName": "[concat('myPublicIp', uniquestring(resourceGroup().id))]",
#     "publicIPAddressType": "Dynamic",
#     "apiVersion": "2015-06-15",
#     "dnsLabelPrefix": "terraform-accexample"
#   },
#   "resources": [
#     {
#       "type": "Microsoft.Storage/storageAccounts",
#       "name": "[variables('storageAccountName')]",
#       "apiVersion": "[variables('apiVersion')]",
#       "location": "[variables('location')]",
#       "properties": {
#         "accountType": "[parameters('storageAccountType')]"
#       }
#     },
#     {
#       "type": "Microsoft.Network/publicIPAddresses",
#       "apiVersion": "[variables('apiVersion')]",
#       "name": "[variables('publicIPAddressName')]",
#       "location": "[variables('location')]",
#       "properties": {
#         "publicIPAllocationMethod": "[variables('publicIPAddressType')]",
#         "dnsSettings": {
#           "domainNameLabel": "[variables('dnsLabelPrefix')]"
#         }
#       }
#     }
#   ],
#   "outputs": {
#     "storageAccountName": {
#       "type": "string",
#       "value": "[variables('storageAccountName')]"
#     }
#   }
# }
# DEPLOY

#   # these key-value pairs are passed into the ARM Template's `parameters` block
#   parameters = {
#     "storageAccountType" = "Standard_GRS"
#   }

#   deployment_mode = "Incremental"
# }

# output "storageAccountName" {
#   value = "${lookup(azurerm_template_deployment.example.outputs, "storageAccountName")}"
# }