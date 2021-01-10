data "external" "glue-job" {
  program = ["python", "${path.module}/glue_job.py"]

  query = {
    aws_region          = "${var.aws_region}"
    job_name            = "${var.job_name}"
    job_role            = "${var.job_role}"
    job_script          = "${var.job_script}"
    job_script_location = "${var.job_script_location}"
    job_tmp_dir         = "${var.job_tmp_dir}"
    job_bookmark_option = "${var.job_bookmark_option}"
    job_language        = "${var.job_language}"
    glue_connections    = "${join(",",var.glue_connections_list)}"
    action_path         = "${path.module}/create.lock"
    job_apply           = "${null_resource.job.id}"
  }
}

