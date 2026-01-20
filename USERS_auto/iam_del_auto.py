import boto3

# Tell Python to talk to the AWS iam service
iam = boto3.client('iam')

#----------------Confirmation----------------------
print("YOU ARE ATTEMPTING TO REMOVE A GROUP")
print("Do you want to proceed ? if 'YES' Type: DeleteUser")
print("If 'NO' press anykey")
sure=input(">: ")
if sure == "DeleteUser":
    print("Proceeding with deletion")
else: 
    print(" Deletion process aborted")
    print(" EXITING !")
    exit()
    
# Variable i created to prompt the username during the print function 
userr= "siv"

# Delete User after policy has been removed
user = iam.delete_user(UserName='siv')
print(f"Deleting user: {userr} ")
print(f"user Deletion Completed: {userr} ")

