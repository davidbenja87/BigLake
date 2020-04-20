resource "azurerm_network_security_group" "nsg" {
  name                = "acceptanceTestSecurityGroup1"
  location            = azurerm_resource_group.my_dev_vnet_alpha_tf_rg.location
  resource_group_name = azurerm_resource_group.my_dev_vnet_alpha_tf_rg.name

  security_rule {
    name                       = "Allow-RDP"
    priority                   = 100
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "Tcp"
    source_port_range          = "*"
    destination_port_range     = "*"
    source_address_prefix      = "*"
    destination_address_prefix = "3389"
  }

  tags = {
    environment = "dev"
  }
}