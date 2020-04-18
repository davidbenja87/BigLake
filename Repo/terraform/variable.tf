variable "ARM_SUBSCRIPTION_ID" {
  default = "974668b8-821d-4cc2-a84d-c81a7733f464"
}

variable "ARM_CLIENT_ID" {
  default = "edda867b-6cce-45e2-8798-d88e91690ad0"
}

variable "ARM_CLIENT_SECRET" {
  default = "Rtbl54usq:G/X2W7OyjAOtp:aUrE:1=7"
}

variable "ARM_TENANT_ID" {
  default = "c8fedfb4-d804-457b-9745-362581de2e4c"
  # default ="b60c9401-2154-40aa-9cff-5e3d1a20085d"
}

variable "storageaccountname" {
  default = "biglakestoragepoctest"
}
variable "location" {
  default = "southindia"
}
variable "environment" {
  default = "dev"
}
variable "my_dev_tf_rg" {
  description = "Resource group for Development"
  default = "my-dev-tf-rg"
}
variable "my_dev_vnet_alpha_tf_rg" {
  description = "Resource group for Development"
  default = "my-dev-vnet-alpha-tf-rg"
}
variable "my_dev_vnet_alpha_addr_space_tf_rg" {
  description = "Resource group for Development"
  default = ["10.1.0.0/16"]
}
variable "my_dev_vnet_alpha_subnet_add_space_tf_rg" {
  description = "Resource group for Development"
  default = ["10.1.0.0/24"]
}
