resource "azurerm_resource_group" "my_dev_tf_rg" {
  name     = var.my_dev_tf_rg
  location = var.location
  
    tags = {
    environment = var.environment
	description = "my resource group"
    terraform = true
  }

}
