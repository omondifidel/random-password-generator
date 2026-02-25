import random

# 1. Keep everything as strings
alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '1234567890'
signs = '!@#$%^&*()_+?<:'

# 2. Combine them
all_chars = alpha + num + signs

length = int(input('Enter the length: '))

# 3. Store the password in a variable
generated_password = ""

for i in range(length):
    generated_password += random.choice(all_chars)

# 4. Now you can use the result whenever you want!
print(f"\nYour new password is: {generated_password}")