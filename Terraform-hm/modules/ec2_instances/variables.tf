variable "ami_id" {
    type = string
  
}

variable "instance_type" {
    type = string
    default = "t3.micro"
  
}

variable "key_name" {
    type = string
    default = "****"
}

variable "subnet_id" {
  type = string
}

variable "vpc_id" {
  type        = string
}

variable "instance_name" {
    type = string
    default = "MyInstance"
}

variable "my_ip" {
    type = string
    default = "*****"
  
}

