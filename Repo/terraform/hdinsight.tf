

# # resource "azurerm_storage_container" "example" {
# #   name                  = "hdinsight"
# #   resource_group_name   = "${azurerm_resource_group.example.name}"
# #   storage_account_name  = "${azurerm_data_lake_store.example.name}"
# #   container_access_type = "private"
# # }

# resource "azurerm_hdinsight_spark_cluster" "example" {
#   name                = "example-hdicluster"
#   resource_group_name = "${azurerm_resource_group.example.name}"
#   location            = "${azurerm_resource_group.example.location}"
#   cluster_version     = "3.6"
#   tier                = "Standard"
# #   dependsOn = [
# #                 "Microsoft.Storage/storageAccounts/test"
# #             ]

#   component_version {
#     spark = "2.3"
#   }

#   gateway {
#     enabled  = true
#     username = "acctestusrgw"
#     password = "TerrAform123!"
#   }

#   storage_account {
#     # storage_container_id = "${azurerm_storage_container.example.id}"
#     # storage_account_key  = "${azurerm_data_lake_store.example.id}"
#     is_default           = false
#   }

#   roles {
#     head_node {
#       vm_size  = "Standard_A3"
#       username = "acctestusrvm"
#       password = "AccTestvdSC4daf986!"
#     }

#     worker_node {
#       vm_size               = "Standard_A3"
#       username              = "acctestusrvm"
#       password              = "AccTestvdSC4daf986!"
#       target_instance_count = 1
#     }

#     zookeeper_node {
#       vm_size  = "Medium"
#       username = "acctestusrvm"
#       password = "AccTestvdSC4daf986!"
#     }
#   }
# }
