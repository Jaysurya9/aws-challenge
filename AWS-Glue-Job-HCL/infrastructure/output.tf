#Add/remove outputs according to infrastructure specified in main (e.g. if a stepfunction is removed, the output for it should also be removed).
output "output" {
	value = "${data.external.glue-job.result}"
}
