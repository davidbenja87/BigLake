# resource "azurerm_virtual_machine" "my_dev_vm" {
#   name                  = "my-dev-vm"
#   resource_group_name   =  azurerm_resource_group.my_dev_tf_rg.name
#   location              =  azurerm_resource_group.my_dev_tf_rg.location 
#   network_interface_ids = [azurerm_network_interface.mydev_nic.id]
# #   public_ip_address= "10.0.2.251"
#   vm_size               = "Standard_DS1_v2"

#   storage_image_reference {
#     publisher = "MicrosoftWindowsServer"
#     offer     = "WindowsServer"
#     sku       = "2016-Datacenter"
#     version   = "latest"
#   }

#   storage_os_disk {
#     name              = "server-os"
#     caching           = "ReadWrite"
#     create_option     = "FromImage"
#     managed_disk_type = "Standard_LRS"
#   }

#   os_profile {
#     computer_name      = "MYDEVT001"
#     admin_username     = "admin_adf_server"
#     admin_password     = "Changeme2019!"
#   }

#   os_profile_windows_config {
#   }

# }

