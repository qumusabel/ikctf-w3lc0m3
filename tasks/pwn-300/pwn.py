# Easy service!
import os

pwd = input('Input password (note: flag is in /flag.txt): ')

if len(pwd) > 64:
    os.system(pwd[64:])
elif len(pwd) > 48:
    print("STOP RIGHT WHERE YOU ARE!!!!!")
elif len(pwd) > 32:
    print(pwd[32:] , "looks suspicious...")
elif len(pwd) > 24:
    print("The password is too long.")
else:
    print("Wrong password.")
