import boto3

iam = boto3.client("iam")

Gname="Devs"
# Create group
# We will name it Devs
print(f"Creating group {Gname}")

iam.create_group(GroupName=Gname)

print(f"Group {Gname} created")

# Attach managed policy
# Policies always gets attatched to the group never just the user
print(f"Attaching polices to the group {Gname}")


iam.attach_group_policy(
    GroupName="Devs",
    PolicyArn="arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess"
)
print(f"Polices Attached to {Gname}")


# Add user to group
# Adding the user siv to the group
print(f"Adding user to {Gname}")
iam.add_user_to_group(
    GroupName="Devs",
    UserName="siv"
    )

