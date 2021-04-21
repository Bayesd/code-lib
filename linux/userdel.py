# https://linuxize.com/post/how-to-delete-users-in-linux-using-the-userdel-command/

username = input("Enter username for user to delete: ")
print("Delete User and User's Home Directory and Mail spool:")
print(f"sudo userdel -r {username}")

print("Delete User only:")
print(f"sudo userdel {username}")
