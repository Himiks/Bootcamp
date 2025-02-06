provider "aws" {
  region = "eu-north-1"
}


module "ec2_instance_1" {
  source        = "./modules/ec2_instances"
  ami_id        = "ami-09a9858973b288bdd"
  instance_type = "t3.micro"
  key_name      = "*****"
  subnet_id     = "subnet-08f2b68b38575da4f"
  vpc_id = "vpc-0111e8320d35de673"
  instance_name = "MyApacheServer1"
  my_ip         = "*****" 
}

module "ec2_instance_2" {
  source        = "./modules/ec2_instances"
  ami_id        = "ami-09a9858973b288bdd"
  instance_type = "t3.micro"
  key_name      = "*****"
  subnet_id     = "subnet-08f2b68b38575da4f"
  vpc_id = "vpc-0111e8320d35de673"
  instance_name = "MyApacheServer2"
  my_ip         = "******"  
}

output "ec2_instance_id" {
  value = module.ec2_instance.instance_id
}

output "ec2_public_ip" {
  value = module.ec2_instance.public_ip
}


