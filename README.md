# Cloud Security AWS IAM & CIS Hardening Lab

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![CI Quality Gate](https://github.com/toprakahmetaydogmus/03-cloudsec-aws-audit/actions/workflows/ci.yml/badge.svg)](https://github.com/toprakahmetaydogmus/03-cloudsec-aws-audit/actions)
[![CIS AWS Benchmark](https://img.shields.io/badge/Compliance-CIS%20AWS%20v1.4-green.svg)](#)
[![Terraform](https://img.shields.io/badge/IaC-Terraform-purple.svg)](#)

Geliştirici: **Toprak Ahmet Aydoğmuş**

---

## 🎯 Proje Amacı ve Kapsamı
AWS bulut altyapılarında **IAM Least Privilege** prensiplerinin uygulanması, S3 kova (bucket) güvenlik politikaları ve CIS AWS Foundations Benchmark kontrollerini otomatize eden güvenlik denetim aracı ve IaC şablonları.

---

## 🏗️ Mimari Şema

```mermaid
graph TD
    TF[Terraform Manifests: main.tf] --> AWS[AWS Cloud / LocalStack Resources]
    Auditor[scripts/cloud_security_auditor.py] -->|JSON Policy AST Parsing| AWS
    Auditor --> Check1[CIS 1.16: Wildcard Action/Resource Audit]
    Auditor --> Check2[CIS 1.20: Unrestricted PassRole Audit]
    Auditor --> Check3[CIS 2.1.5: S3 Public Access Block Audit]
    Check1 --> Report[Security & Compliance Findings Report]
    Check2 --> Report
    Check3 --> Report
```

---

## 🚀 Güvenlik Kontrolleri
- **CIS 1.16:** IAM politikalarında `*:*` (Wildcard) yönetici yetkisi denetimi.
- **CIS 1.20:** `iam:PassRole` eyleminin tüm kaynaklara (`*`) verilerek yetki yükseltme vektörü oluşturmasının engellenmesi.
- **CIS 2.1.5:** S3 kova genel erişim engelleme (Public Access Block) ve varsayılan KMS şifreleme kontrolü.

---

## ⚡ Hızlı Başlangıç

```bash
git clone https://github.com/toprakahmetaydogmus/03-cloudsec-aws-audit.git
cd 03-cloudsec-aws-audit

# Unit testleri çalıştırın
python -m unittest discover tests/

# Bulut güvenlik denetim aracını çalıştırın
python scripts/cloud_security_auditor.py
```

---

## 📜 Lisans
MIT License - **Toprak Ahmet Aydoğmuş**
