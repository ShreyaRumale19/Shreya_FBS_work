# Correct user ID and password
correct_userid = "Shreya"
correct_password = "1234"

userid = input("Enter User ID: ")
password = input("Enter Password: ")


if userid == correct_userid and password == correct_password:
    print("Login Successful")
else:
    print("Invalid User ID or Password ")