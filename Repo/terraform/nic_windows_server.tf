resource "azurerm_network_interface" "mydev_nic" {
  name                = "my-dev-nic"
  location            = azurerm_resource_group.my_dev_vnet_alpha_tf_rg.location
  resource_group_name = azurerm_resource_group.my_dev_vnet_alpha_tf_rg.name
  
  ip_configuration {
    name                          = "mydevvmconfig"
    subnet_id                     = var.subnet_private
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id=azurerm_public_ip.publicip.id
    
    # public_ip_addresses  = "10.0.2.251"
    # public_ip_address= "10.0.2.251"
 
  }
  network_security_group_id = var.nsg


}
