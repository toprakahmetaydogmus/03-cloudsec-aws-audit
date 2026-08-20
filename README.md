# ☁️ Cloud Security AWS IAM & CIS Hardening Lab

[![GitHub release (latest by date)](https://img.shields.io/github/v/release/toprakahmetaydogmus/03-cloudsec-aws-audit?color=blue&label=Release)](https://github.com/toprakahmetaydogmus/03-cloudsec-aws-audit/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![CIS Benchmark](https://img.shields.io/badge/CIS%20AWS%20Benchmark-v1.4.0-brightgreen.svg)](#)

Developer: **Toprak Ahmet Aydoğmuş**

---

## 🎯 1. Overview
Automated AWS Cloud Security posture evaluation engine implementing the **CIS AWS Foundations Benchmark v1.4.0**. Audits IAM privilege escalation paths, overly permissive S3 buckets, unencrypted EBS volumes, Security Group misconfigurations, and root account activity.

---

## 🚀 2. Quick Start

```bash
git clone https://github.com/toprakahmetaydogmus/03-cloudsec-aws-audit.git
cd 03-cloudsec-aws-audit

# Run audit tests
python -m unittest discover tests/

# Run the AWS IAM & CIS Auditor
python -m src.aws_auditor --report html
```

---

## 📜 3. License
Licensed under the [MIT License](LICENSE).  
Developer: **Toprak Ahmet Aydoğmuş**.
