variable "aws_region" {
  type        = string
  description = "AWS region"
  default = "eu-west-1"
}

variable "vpc_name" {
  type        = string
  description = "Name of the VPC to be used for the glue jobs"
  default = "glue_vpc"
}

variable "job_name" {
  type        = string
  description = "Job Name"
  default = "my_job"
}

variable "job_role" {
  type        = string
  description = "Job Role"
  default = "arn:aws:iam::111111111111:role/my_role"
}

variable "job_script" {
  description = "Job Script"
  default = ""
}

variable "job_script_location" {
  description = "Job Script Location"
  default = ""
}

variable "job_tmp_dir" {
  description = "Job Temporary Directory"
  default = ""
}
   
variable "job_bookmark_option" {
  description = "Job BookMark Option"
  default = ""
}

variable "job_language" {
  description = "Job Language"
  default     = "python"
}

variable "glue_connections_list" {
  description = "Glue Connection"
  type        = "list"
}
