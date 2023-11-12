import random
characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
password_length = 7
password = ""

for i in range(password_length):
    password += random.choice(characters)
print("Your password is: ", password)