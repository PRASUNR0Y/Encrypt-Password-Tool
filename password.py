# Shuffle of abcdefghijklmnopqrstuvwxyz1234567890@#$%^&
meth = "mpalh23b@9usd^8f#$wvci&r0gj1qn6ox7tzek4%5y"

password = input("Enter password: \n")
encryption = ""
for val in password:
  encryption += meth[((ord(val)*50+2)%len(meth))]

print("Encoded Password is :",encryption)