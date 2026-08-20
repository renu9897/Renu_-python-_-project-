import re

print("=== PASSWORD STRENGTH CHECKER ===")
pwd = input("Apna password dalo: ")

score = 0
feedback = []

# Check 1
if len(pwd) >= 8:
    score += 1
else:
    feedback.append("-> 8 characters se chota hai")

# Check 2
if re.search(r"[A-Z]", pwd):
    score += 1
else:
    feedback.append("-> Capital letter (A-Z) nahi hai")

# Check 3
if re.search(r"[a-z]", pwd):
    score += 1
else:
    feedback.append("-> Small letter (a-z) nahi hai")

# Check 4
if re.search(r"[0-9]", pwd):
    score += 1
else:
    feedback.append("-> Number (0-9) nahi hai")

# Check 5
if re.search(r"[!@#$%^&*]", pwd):
    score += 1
else:
    feedback.append("-> Special symbol (!@#$) nahi hai")

print(f"\nScore: {score}/5")

if score == 5:
    print("STRONG PASSWORD - Koi hack nahi kar payega! 💪")
elif score >= 3:
    print("MEDIUM - Thik hai par aur strong banao")
else:
    print("WEAK - 2 sec me hack ho jayega! ❌")

if feedback:
    print("\nSudhar karo:")
    for f in feedback:
        print(f)