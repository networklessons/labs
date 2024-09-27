terraform {
  required_providers {
    iosxe = {
      source = "CiscoDevNet/iosxe"
    }
  }
}

provider "iosxe" {
  username = "cisco"
  password = "cisco"
  url      = "https://10.65.90.202"
}

resource "iosxe_interface_loopback" "example" {
  name                = 100
  description         = "My Terraform Created Loopback"
  shutdown            = false
  ipv4_address        = "1.1.1.1"
  ipv4_address_mask   = "255.255.255.255"
}