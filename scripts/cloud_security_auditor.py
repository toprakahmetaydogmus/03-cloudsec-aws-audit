#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AWS IAM & S3 Security Posture Auditor
Author: Toprak Ahmet Aydoğmuş
"""

import json
from typing import Dict, List, Any

class AWSCloudAuditor:
    def __init__(self):
        self.findings: List[Dict[str, Any]] = []

    def audit_iam_policy(self, policy_name: str, policy_doc: Dict[str, Any]):
        statements = policy_doc.get("Statement", [])
        if isinstance(statements, dict):
            statements = [statements]

        for stmt in statements:
            effect = stmt.get("Effect")
            actions = stmt.get("Action", [])
            resources = stmt.get("Resource", [])

            if isinstance(actions, str):
                actions = [actions]
            if isinstance(resources, str):
                resources = [resources]

            # Check 1: Full Administrator Privileges (*:*)
            if effect == "Allow" and "*" in actions and "*" in resources:
                self.findings.append({
                    "resource": policy_name,
                    "severity": "CRITICAL",
                    "check": "CIS-AWS-1.16",
                    "description": "IAM Policy grants wildcard Action and Resource (*:*). Violates Least Privilege."
                })
            # Check 2: Missing Resource scoping
            elif effect == "Allow" and "*" in resources and any("PassRole" in a for a in actions):
                self.findings.append({
                    "resource": policy_name,
                    "severity": "HIGH",
                    "check": "CIS-AWS-1.20",
                    "description": "iam:PassRole allowed on all resources (*). Potential Privilege Escalation vector."
                })

    def audit_s3_bucket(self, bucket_name: str, config: Dict[str, Any]):
        if not config.get("block_public_access", False):
            self.findings.append({
                "resource": f"s3://{bucket_name}",
                "severity": "CRITICAL",
                "check": "CIS-AWS-2.1.5",
                "description": "S3 Public Access Block is disabled. Bucket is potentially exposed."
            })
        if not config.get("server_side_encryption", False):
            self.findings.append({
                "resource": f"s3://{bucket_name}",
                "severity": "MEDIUM",
                "check": "CIS-AWS-2.1.1",
                "description": "Default server-side encryption (KMS/AES256) is not enforced."
            })

if __name__ == "__main__":
    auditor = AWSCloudAuditor()
    print("[*] Starting AWS Cloud Security Configuration Audit...")
    
    # Sample test policies
    vulnerable_iam = {
        "Version": "2012-10-17",
        "Statement": [{"Effect": "Allow", "Action": "*", "Resource": "*"}]
    }
    secure_iam = {
        "Version": "2012-10-17",
        "Statement": [{"Effect": "Allow", "Action": ["s3:GetObject"], "Resource": "arn:aws:s3:::app-data/*"}]
    }

    auditor.audit_iam_policy("VulnerableDevRolePolicy", vulnerable_iam)
    auditor.audit_iam_policy("SecureAppRolePolicy", secure_iam)
    auditor.audit_s3_bucket("customer-records-raw", {"block_public_access": False, "server_side_encryption": False})
    auditor.audit_s3_bucket("audit-logs-encrypted", {"block_public_access": True, "server_side_encryption": True})

    print(f"[+] Audit Finished. Found {len(auditor.findings)} security findings:\n")
    for f in auditor.findings:
        print(f"  [{f['severity']}] [{f['check']}] {f['resource']}: {f['description']}")
