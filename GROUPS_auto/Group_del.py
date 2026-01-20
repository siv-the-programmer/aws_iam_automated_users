import boto3

iam = boto3.client("iam")

#----------------Confirmation----------------------
print("YOU ARE ATTEMPTING TO REMOVE A GROUP")
print("Do you want to proceed ? if 'YES' Type: DeleteGroup")
print("If 'NO' press anykey")
sure=input(">: ")
if sure == "DeleteGroup":
    print("Proceeding with deletion")
else: 
    print(" Deletion process aborted")
    print(" EXITING !")
    exit()

    
# My variable for the group name
Gname="Devs"

# Delete user from group
# Deleting the user siv from the group
print(f"Deleting user from {Gname}")
iam.remove_user_from_group(
    GroupName="Devs",
    UserName="siv"
    )

# detach managed policies
# Policies always gets detatched from the group never just the user
print(f"detaching polices from the group {Gname}")
pol=iam.detach_group_policy(
    GroupName="Devs",
    PolicyArn="arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess"
)

if not pol:
    pass
    print("No polices to remove")
    print("Moving on")
else:
    print(f"Polices detached from {Gname}")


# Delete the group
# add the group name if no variable used
print(f"Deleting group {Gname}")
gr=iam.delete_group(GroupName=Gname)
print(f"Group {Gname} deleted")

if not gr:
    print("No group to delete")
    exit()
else:
    pass


