

provider "azurerm" {

  subscription_id = "${var.ARM_SUBSCRIPTION_ID}"
  client_id       = "${var.ARM_CLIENT_ID}"
  client_secret   = "${var.ARM_CLIENT_SECRET}"
  tenant_id       = "${var.ARM_TENANT_ID}"
}

resource "azurerm_resource_group" "example" {
  name     = "example"
  location = "northeurope"
}

resource "azurerm_data_lake_store" "example" {
  name                = "biglakedatagen"
  resource_group_name = "${azurerm_resource_group.example.name}"
  location            = "${azurerm_resource_group.example.location}"
  encryption_state    = "Enabled"
  encryption_type     = "ServiceManaged"
  firewall_allow_azure_ips = "Disabled"
  firewall_state = "Disabled"
}

# resource "azurerm_databricks_workspace" "example" {
#   name                = "databricks-test"
#   resource_group_name = "${azurerm_resource_group.example.name}"
#   location            = "${azurerm_resource_group.example.location}"
#   sku                 = "standard"

#   tags = {
#     Environment = "Production"
#   }
# }