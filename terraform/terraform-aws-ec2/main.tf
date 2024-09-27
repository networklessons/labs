provider "aws" {
  region = "us-west-2"  # Set your desired AWS region
}

resource "aws_instance" "example" {
  ami           = "ami-0819177b8e6d4947a"  # Ubuntu 24.04 LTS
  instance_type = "t2.nano"

  tags = {
    Name = "my-aws-terraform-ec2-instance"
  }
}