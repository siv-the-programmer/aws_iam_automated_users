import boto3

iam = boto3.client('iam')

# Variable i created to prompt the username during the print function 
user1 = "siv"

# Create User you would like to add
user = iam.create_user(UserName=user1)
print(f"Creating user {user1} ")


# List of policies to attach to the user
policies = [
    'arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess',
    'arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess'
]


# Attach all policies in the list to the user
for policy_arn in policies:
    iam.attach_user_policy(
        UserName=user1,
        PolicyArn=policy_arn
    )


print(f"attaching policies to user {user1}")
print(f"All policies attached to {user1} successfully.")


print(f"attaching policies to user {user1}")
print(f"User {user1} successfully created")


# Shows how many polices were added and also shows the names of the polices added.
# You may activate it if you need it
"""
rem=input("Would you like to view polices added? y/n >: ")
if rem == "y":
    print(f"Added {len(policies)} {policies} policies from {user1}") 
else: 
    print("done")

"""