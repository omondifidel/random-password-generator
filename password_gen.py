import random

# Your character pool
alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '1234567890'
signs = '!@#$%^&*()_+?<:'
all_chars = alpha + num + signs

# --- VALIDATION START ---
while True:
    try:
        length = int(input('Enter password length (minimum 8): '))
        
        if length < 1:
            print("❌ You can't have a password with no length!")
        elif length < 8:
            print("⚠️ That's a bit short for security! Let's try 8 or more.")
        else:
            # Everything is perfect
            break
            
    except ValueError:
        print("❌ Invalid input! Please enter a whole number (e.g., 12).")
# --- VALIDATION END ---

# Generate the password
password = "".join(random.choice(all_chars) for i in range(length))

print("-" * 30)
print(f"🔒 Your Secure Password: {password}")
print("-" * 30)