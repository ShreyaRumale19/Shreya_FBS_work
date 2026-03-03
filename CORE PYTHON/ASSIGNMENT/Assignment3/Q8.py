correct_userid = "Shreya"
correct_password = "1234"

# Ask user for login
userid = input("Enter User ID: ")
password = input("Enter Password: ")

if userid == correct_userid and password == correct_password:
    print("Login Successful!")
    
    # Fixed 4-digit number (captcha)
    number = "5678"
    print("Enter this number to continue:", number)
    
    user_number = input("Re-enter the number: ")
    
    if user_number == number:
        print("Verification Successful ")
    else:
        print("Verification Failed")
else:
    print("Invalid User ID or Password ")