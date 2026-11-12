correct_otp = "1234"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    otp = input("Enter OTP: ").strip()

    if otp == "":
        pass
        continue

    attempts += 1

    if otp == correct_otp:
        print("Login Successful")
        break
    else:
        print("Incorrect OTP")

else:
    print("Account locked for 30 minutes")
