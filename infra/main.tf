variable "aws_region" {
  type        = string
  description = "AWS region for the lab resource"
}

variable "parameter_name" {
  type        = string
  description = "SSM parameter path owned by this experiment"
}

variable "parameter_value" {
  type        = string
  description = "Desired non-sensitive SSM parameter value"
  default     = "desired-v1"
}

resource "aws_ssm_parameter" "drift_proof" {
  name        = var.parameter_name
  description = "lab1_agent persistent IaC drift proof"
  type        = "String"
  value       = var.parameter_value
  overwrite   = true

  tags = {
    project = "lab1-agent"
    purpose = "oidc-iac-drift-proof"
  }
}
