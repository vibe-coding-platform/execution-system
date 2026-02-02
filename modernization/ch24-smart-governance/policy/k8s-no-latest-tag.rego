package kubernetes.images

default allow = false

# Allow only if none of the containers use :latest tag
allow {
  input.kind == "Deployment"
  containers := input.spec.template.spec.containers
  not some c in containers
  endswith(c.image, ":latest")
}
