resource "null_resource" "job" {
  provisioner "local-exec" {
    when    = "create"
    command = "touch ${path.module}/create.lock"
  }

  provisioner "local-exec" {
    when    = "destroy"
    command = "python ${path.module}/glue_job_destroy.py ${var.job_name} ${var.aws_region}"
  }
}
