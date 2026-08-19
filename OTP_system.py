# otp_system.py
import random

def generate_otp():
    otp = random.randint(1000, 9999)
    return otp

print("--- OTP System ---")
generated_otp = generate_otp()
print(f"Your OTP is: {generated_otp}")  # Real me ye SMS/Email pe jata hai

user_otp = int(input("Enter OTP to verify: "))

if user_otp == generated_otp:
    print("OTP Verified! Login Successful ✅")
else:
    print("Wrong OTP! Try Again ❌")