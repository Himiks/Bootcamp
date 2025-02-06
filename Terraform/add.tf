
resource "aws_security_group" "HlibSG" {
    name = "MySecurityGroup"
    vpc_id      = data.aws_subnet.selected.vpc_id
    dynamic "ingress" {
        for_each = var.ingress_rules
        content {
            from_port = ingress.value
            to_port = ingress.value
            protocol = "tcp"
            cidr_blocks = ["0.0.0.0/0"]
        }

    }

    egress {
        from_port = 0
        to_port = 0
        protocol = -1
        cidr_blocks = ["0.0.0.0/0"]
    }

}



data "aws_ami" "latest" {
    most_recent = true
    owners = ["amazon"]

    filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
  }
}



resource "aws_instance" "MyInstance" {
  ami           = data.aws_ami.latest.id
  instance_type = "t3.micro"
  subnet_id     = "subnet-09cc1026f668efeda"
  vpc_security_group_ids = [aws_security_group.HlibSG.id]

  user_data = filebase64("website.sh")

  tags = {
    Name = "MyInstance"
  }
}

output "public_ip" {
    description = "The public IP address"
    value = aws_instance.MyInstance.public_ip

}

                           