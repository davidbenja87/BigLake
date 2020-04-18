# resource "azurerm_resource_group" "example" {
#   name     = "acceptanceTestResourceGroup1"
#   location = "West US"
# }

# resource "azurerm_network_security_group" "example" {
#   name                = "acceptanceTestSecurityGroup1"
#   location            = azurerm_resource_group.example.location
#   resource_group_name = azurerm_resource_group.example.name
# }

# resource "azurerm_network_ddos_protection_plan" "example" {
#   name                = "ddospplan1"
#   location            = azurerm_resource_group.example.location
#   resource_group_name = azurerm_resource_group.example.name
# }

# resource "azurerm_virtual_network" "example" {
#   name                = "virtualNetwork1"
#   location            = azurerm_resource_group.example.location
#   resource_group_name = azurerm_resource_group.example.name
#   address_space       = ["10.0.0.0/16"]
#   dns_servers         = ["10.0.0.4", "10.0.0.5"]

#   ddos_protection_plan {
#     id     = azurerm_network_ddos_protection_plan.example.id
#     enable = true
#   }

#   subnet {
#     name           = "subnet1"
#     address_prefix = "10.0.1.0/24"
#   }

#   subnet {
#     name           = "subnet2"
#     address_prefix = "10.0.2.0/24"
#   }

#   subnet {
#     name           = "subnet3"
#     address_prefix = "10.0.3.0/24"
#     security_group = azurerm_network_security_group.example.id
#   }

#   tags = {
#     environment = "Production"
#   }
# }

resource "azurerm_virtual_network" "my_dev_vnet_alpha" {
  name                = "virtualNetworkalpha"
  location            = azurerm_resource_group.my_dev_vnet_alpha_tf_rg.location
  resource_group_name = azurerm_resource_group.my_dev_vnet_alpha_tf_rg.name
  address_space       = ["10.0.0.0/16"]
  subnet {
    name           = "private"
    address_prefix = "10.0.1.0/24"
  }
  subnet {
    name           = "public"
    address_prefix = "10.0.2.0/24"
  }
}