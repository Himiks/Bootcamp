output "instance_id" {
  value       = aws_instance.web.id
}

output "public_ip" {
  value       = aws_instance.web.public_ip
}

output "web_url" {
  value       = "http://${aws_instance.web.public_ip}"
}
