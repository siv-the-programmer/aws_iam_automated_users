import boto3

iam = boto3.client('iam')

# Variable i created to prompt the username during the print function 
user1 = "siv"

# Create User you would like to add
user = iam.create_user(UserName=user1)
print(f"Creating user {user1} ")


print(f"User {user1} successfully created")

