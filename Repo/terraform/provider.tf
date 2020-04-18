# provider "azurerm" {
#   subscription_id = "974668b8-821d-4cc2-a84d-c81a7733f464"
#   client_id       = "edda867b-6cce-45e2-8798-d88e91690ad0"
#   client_secret   = "Rtbl54usq:G/X2W7OyjAOtp:aUrE:1=7"
#   tenant_id       = "c8fedfb4-d804-457b-9745-362581de2e4c"
#   version = "=2.6"
# }

provider "azurerm" {
    version = "=1.42"
    subscription_id = var.ARM_SUBSCRIPTION_ID
    client_id       = var.ARM_CLIENT_ID
    client_secret   = var.ARM_CLIENT_SECRET
    tenant_id       = var.ARM_TENANT_ID
}
