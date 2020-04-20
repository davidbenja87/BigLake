resource "azurerm_public_ip" "publicip" {
  name                    = "test-pip"
  location                = azurerm_resource_group.my_dev_vnet_alpha_tf_rg.location
  resource_group_name     = azurerm_resource_group.my_dev_vnet_alpha_tf_rg.name
  allocation_method       = "Dynamic"
  idle_timeout_in_minutes = 30

  tags = {
    environment = "test"
  }
}