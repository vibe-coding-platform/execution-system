# Ch24 Smart Governance ✅

**Pre-commit configs + Policy-as-code templates + Governance portal.**

## 1. Pre-commit Configs

- `.pre-commit-config.yaml` → standardize checks
- `hooks/snowflake_policy.py` → block obvious AI snowflake code

Usage:

```bash
pip install pre-commit
pre-commit install
pre-commit run --all-files
2. Policy-as-Code (OPA / Rego)
policy/k8s-no-latest-tag.rego → forbids :latest images

policy/terraform-no-public-s3.rego → forbids public S3 buckets

Run in CI or locally with opa eval.

3. Governance Slice in Portal
portal/governance.tsx → shows:

Pre-commit coverage

Policy-compliant pipelines

Direct prod changes (should be 0)

Goal: 90%+ repos with pre-commit + policies enforced before prod.

