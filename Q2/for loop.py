correct_otp = "1234"

for attempt in range(3):

    while True:
        otp = input("Enter OTP: ").strip()

        if otp == "":
            print("Blank input. Try again.")
            continue

        break

    if otp == correct_otp:
        print("Login Successful")
        break

    print("Incorrect OTP")

else:
    print("Account locked for 30 minutes")
