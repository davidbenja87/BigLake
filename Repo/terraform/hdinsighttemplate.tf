resource "azurerm_template_deployment" "hdinsight" {
  name                = "acctesttemplate-02"
  resource_group_name = "${azurerm_resource_group.example.name}"


 template_body = <<DEPLOY
{
  "$schema": "http://schema.management.azure.com/schemas/2014-04-01-preview/deploymentTemplate.json#",
  "contentVersion": "1.0.0.0",
  "parameters": {
    "clusterName": {
      "type": "string",
      "defaultValue": "biglakehdinsight",
       "metadata": {
        "description": "The name of the HDInsight cluster to create."
      }
    },
    "identityCertificate": {
            "type": "securestring",
            "defaultValue":null
    },
    "identityCertificatePassword": {
            "type": "securestring",
            "defaultValue":null
    }
  },
  "variables": {
    "location": "[resourceGroup().location]",
    "clusterLoginUserName":"admin",
    "clusterLoginPassword": "London20!8",
    "clusterVersion":"3.6",
    "clusterWorkerNodeCount":1,
    "clusterKind":"SPARK",
    "sshUserName":"sshuser",
    "sshPassword":"London20!8",
    "apiVersion": "2015-03-01-preview"
  },

  "resources": [
    {
      "type": "Microsoft.Storage/storageAccounts",
      "name": "[parameters('clusterName')]",
      "apiVersion": "[variables('apiVersion')]",
      "location": "[variables('location')]",
      "dependsOn": [],
      "properties": {
        "clusterVersion": "[variables('clusterVersion')]", 
        "osType": "Linux",
        "tier": "standard", 
        "clusterDefinition": {
                    "kind": "[variables('clusterKind')]",
                    "componentVersion": {
                        "Spark": "2.3"
                },
                "configurations": {
                    "gateway": {
                        "restAuthCredential.isEnabled": true,
                        "restAuthCredential.username": "[variables('clusterLoginUserName')]",
                        "restAuthCredential.password": "[variables('clusterLoginPassword')]"
                    },
                    "core-site": {
                        "fs.defaultFS": "adl://home",
                        "dfs.adls.home.hostname": "biglakedatagen.azuredatalakestore.net",
                        "dfs.adls.home.mountpoint": "/"
                    },
                    "clusterIdentity": {
                        "clusterIdentity.applicationId": "b9dfcab9-a3fa-4c7b-8dc5-857c83ff054c",
                        "clusterIdentity.certificate": "[parameters('identityCertificate')]",
                        "clusterIdentity.aadTenantId": "https://login.windows.net/c8fedfb4-d804-457b-9745-362581de2e4c",
                        "clusterIdentity.resourceUri": "https://datalake.azure.net/",
                        "clusterIdentity.certificatePassword": "[parameters('identityCertificatePassword')]"
                    }
                }
        },
        "storageProfile": {
                    "storageaccounts": []
        },
         "computeProfile": {
            "roles": [
                {
                    "autoscale": null,
                    "name": "headnode",
                    "minInstanceCount": 1,
                    "targetInstanceCount": 2,
                    "hardwareProfile": {
                        "vmSize": "Standard_D12_V2"
                    },
                    "osProfile": {
                        "linuxOperatingSystemProfile": {
                            "username": "[variables('sshUserName')]",
                            "password": "[variables('sshPassword')]"
                        }
                    },
                    "virtualNetworkProfile": null,
                    "scriptActions": [],
                    "dataDisksGroups": null
                },
                {
                    "autoscale": null,
                    "name": "workernode",
                    "targetInstanceCount": 1,
                    "hardwareProfile": {
                        "vmSize": "Standard_D13_V2"
                    },
                    "osProfile": {
                        "linuxOperatingSystemProfile": {
                            "username": "[variables('sshUserName')]",
                            "password": "[variables('sshPassword')]"
                        }
                    },
                    "virtualNetworkProfile": null,
                    "scriptActions": [],
                    "dataDisksGroups": null
                }
            ]
        }
      }
    }

   ]
     
}
      
      
DEPLOY

  # these key-value pairs are passed into the ARM Template's `parameters` block
  parameters = {
    "clusterName" = "biglakehdinsight"
  }

  deployment_mode = "Incremental"
}
