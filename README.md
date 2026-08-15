# Cloud Security AWS IAM & CIS Hardening Lab
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Terraform](https://img.shields.io/badge/IaC-Terraform-purple.svg)](#)
[![CIS AWS](https://img.shields.io/badge/Compliance-CIS%20AWS%20Benchmark-green.svg)](#)

Geliştirici: **Toprak Ahmet Aydoğmuş**

Bu proje; AWS bulut ortamlarında **IAM Least Privilege**, S3 Public Access engelleme ve CloudTrail denetimlerini otomatikleştiren bir Cloud Security posture yönetim aracıdır.

## Mimari
```mermaid
graph TD
    TF[Terraform Infrastructure] --> Cloud[AWS Resources: IAM, S3, KMS]
    Auditor[cloud_security_auditor.py] -->|Evaluate JSON Policies| Cloud
    Auditor -->|Flag Over-Permissive Rules| Report[CIS Benchmark Compliance Report]
```

## Hızlı Başlangıç
```bash
# Python güvenlik denetim motorunu çalıştırın
python3 scripts/cloud_security_auditor.py
```

## Lisans
MIT License - Toprak Ahmet Aydoğmuş
