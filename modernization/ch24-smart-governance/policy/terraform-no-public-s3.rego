package terraform.aws.s3

default allow_public = false

allow_public {
  some r in input.resource.aws_s3_bucket
  r.acl == "public-read"  # or "public-read-write"
}
## Run policies locally (example)

```bash
opa eval --input k8s-deployment.json --data policy/k8s-no-latest-tag.rego "data.kubernetes.images.allow"
