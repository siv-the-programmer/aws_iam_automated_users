AWS IAM Automation – Python & Boto3
--

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![AWS IAM](https://img.shields.io/badge/AWS-IAM-orange?logo=amazonaws&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-Cloud-orange?logo=amazonaws&logoColor=white)
![Boto3](https://img.shields.io/badge/Boto3-AWS%20SDK-yellow)
![Automation](https://img.shields.io/badge/Focus-Automation-green)




This repository demonstrates hands-on experience automating AWS Identity and Access Management (IAM) tasks using Python and boto3. The scripts showcase my ability to create, manage, and remove IAM users programmatically, applying real-world AWS best practices for security, automation, and policy management.

About This Project
---


Managing IAM users manually through the AWS Console can be repetitive and error-prone. These scripts automate the process, giving precise control over user creation, policy assignment, and user deletion. This reflects my focus on:

AWS Core Services: IAM, S3, EC2

Automation Skills: Python scripting for cloud operations

Security Awareness: Detaching policies before user deletion, following least-privilege principles

Practical AWS Learning: Hands-on implementation of AWS best practices

# Folder 
```
USERS_Auto

 1. iam_add_auto.py
```
Automates the creation of an IAM user and attaches predefined AWS managed policies.
<img src="awspics/pic1.png" width="400" alt="addpic">

# Check if user exists
```
aws iam list-users
```

<img src="awspics/pic3.png" width="400" alt="addpic">

# Confirm in AWSCONSOLE if user is there

<img src="awspics/pic4.png" width="400" alt="addpic">



# Key Features:

Creates a user dynamically via Python variable

Attaches multiple AWS managed policies for S3 and EC2 read-only access

# Optionally lists attached policies for verification

<img src="awspics/pic2.png" width="400" alt="addpol">

Confirm in AWSCONSOLE if policies were added

<img src="awspics/pic5.png" width="400" alt="addpol">

# NB: Never add polices to users directly, always add to the group then put the user in the group




# Folder
```
USERS_auto

2. iam_del_auto.py
```
- Created a confirmation prompt to confirm deletion for safety.

---

# Folder 2
```
GROUPS_auto
```
```
1. Group_add.py
```
- Creates a group of your choice
- Adds Policies you want
- adds a user of choice to the group

```
2. Group_del.py
```
- Prompts confirmation in order to delete anything
- Removes user out of group
- Detatches polices
- Deletes group and prints confirmation
Key Features:
--

Deletes IAM users programmatically

Optional output of removed policies


Skills Demonstrated
--
AWS Automation: Using boto3 to interact with IAM programmatically

Python Scripting: Writing reusable, readable, and modular automation scripts

Security Mindset: Ensuring policies are detached before deletion, avoiding destructive errors

Cloud Engineering Fundamentals: Hands-on experience with AWS IAM, S3, and EC2 concepts

# Prerequisites
```
Python 3.x

boto3 installed (pip install boto3)

AWS CLI configured with credentials that have sufficient IAM permissions (aws configure)

Required IAM Permissions:

iam:CreateUser

iam:AttachUserPolicy

iam:DetachUserPolicy

iam:DeleteUser
```

Best Practices
---

Use the iam_del_auto with caution as it does not prompt

Test in a sandbox or non-production account before production usage

Follow the principle of least privilege for IAM operations


This project is part of my continuous learning path toward AWS proficiency, combining Python automation, cloud security, and hands-on AWS management skills.

Portfolio
https://sivb-linklet-123.s3.us-east-1.amazonaws.com/index.html
