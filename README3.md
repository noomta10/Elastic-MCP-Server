# Project Void: Infrastructure as Code
This repository contains Terraform scripts for deploying the cloud environment.

## Deployment
1. Run `terraform init`
2. Run `terraform apply`

## Cloud Provider
Currently configured for AWS (Amazon Web Services) in the `us-east-1` region. It sets up a VPC, three subnets, and an S3 bucket for logging.