import boto3

# Tell Python to talk to the AWS iam service
iam = boto3.client('iam')

# Variable i created to prompt the username during the print function 
userr= "siv"

# detach the policies off the user
# do this first before deleting the user or you will get a error
# List of policies to detach off the user
policies = [
    'arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess',
    'arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess'
]


# detach all policies in the list to the user
for policy_arn in policies:
    iam.detach_user_policy(
        UserName=userr,
        PolicyArn=policy_arn
    )
    
if policies == []:
    print("no policies to detach")
else:
    print(f"Removing policies from user: {userr} ")
    

# Delete User after policy has been removed
user = iam.delete_user(UserName='siv')
print(f"Deleting user: {userr} ")
print(f"user Deletion Completed: {userr} ")

# SHows the number of polices that was removed and the names
"""
rem=input("Would you like to view polices removed? y/n >: ")
if rem == "y":
    print(f"Removed {len(policies)} {policies} policies from {userr}") 
else: 
    print("done")
    
"""    

