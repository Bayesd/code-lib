# https://linuxize.com/post/how-to-create-users-in-linux-using-the-useradd-command/

username = input("Enter username for new user: ")
print()
print("Add a New User with Home Directory:\n")
print(f"sudo useradd -m {username} && sudo passwd {username}")



