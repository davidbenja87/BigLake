resource "azurerm_template_deployment" "hdinsight" {
  name                = "acctesttemplate-02"
  resource_group_name = "${azurerm_resource_group.example.name}"


 template_body = <<DEPLOY
{
    "$schema": "http://schema.management.azure.com/schemas/2014-04-01-preview/deploymentTemplate.json#",
    "contentVersion": "0.9.0.0",
    "parameters": {
        "clusterName": {
            "type": "string",
            "metadata": {
                "description": "The name of the HDInsight cluster to create."
            }
        },
        "clusterLoginUserName": {
            "type": "string",
            "defaultValue": "admin",
            "metadata": {
                "description": "These credentials can be used to submit jobs to the cluster and to log into cluster dashboards."
            }
        },
        "clusterLoginPassword": {
            "type": "securestring",
            "metadata": {
                "description": "The password must be at least 10 characters in length and must contain at least one digit, one non-alphanumeric character, and one upper or lower case letter."
            }
        },
        "location": {
            "type": "string",
            "defaultValue": "eastus2",
            "metadata": {
                "description": "The location where all azure resources will be deployed."
            }
        },
        "clusterVersion": {
            "type": "string",
            "defaultValue": "3.6",
            "metadata": {
                "description": "HDInsight cluster version."
            }
        },
        "clusterWorkerNodeCount": {
            "type": "int",
            "defaultValue": 1,
            "metadata": {
                "description": "The number of nodes in the HDInsight cluster."
            }
        },
        "clusterKind": {
            "type": "string",
            "defaultValue": "SPARK",
            "metadata": {
                "description": "The type of the HDInsight cluster to create."
            }
        },
        "sshUserName": {
            "type": "string",
            "defaultValue": "sshuser",
            "metadata": {
                "description": "These credentials can be used to remotely access the cluster."
            }
        },
        "sshPassword": {
            "type": "securestring",
            "metadata": {
                "description": "The password must be at least 10 characters in length and must contain at least one digit, one non-alphanumeric character, and one upper or lower case letter."
            }
        },
        "identityCertificate": {
            "type": "securestring"
        },
        "identityCertificatePassword": {
            "type": "securestring"
        }
    },
    "resources": [
        {
            "apiVersion": "2015-03-01-preview",
            "name": "[parameters('clusterName')]",
            "type": "Microsoft.HDInsight/clusters",
            "location": "[parameters('location')]",
            "dependsOn": [],
            "properties": {
                "clusterVersion": "[parameters('clusterVersion')]",
                "osType": "Linux",
                "tier": "standard",
                "clusterDefinition": {
                    "kind": "[parameters('clusterKind')]",
                    "componentVersion": {
                        "Spark": "2.3"
                    },
                    "configurations": {
                        "gateway": {
                            "restAuthCredential.isEnabled": true,
                            "restAuthCredential.username": "[parameters('clusterLoginUserName')]",
                            "restAuthCredential.password": "[parameters('clusterLoginPassword')]"
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
                                    "username": "[parameters('sshUserName')]",
                                    "password": "[parameters('sshPassword')]"
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
                                    "username": "[parameters('sshUserName')]",
                                    "password": "[parameters('sshPassword')]"
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
    "clusterName" = "biglakehdinsight",
    "clusterLoginPassword" = "London20!8",
    "identityCertificate"="${file("arm/azuredeploy.json")}",
    "identityCertificatePassword"="London20!8",
    "sshPassword"="London20!8"

  }

  deployment_mode = "Incremental"
}
