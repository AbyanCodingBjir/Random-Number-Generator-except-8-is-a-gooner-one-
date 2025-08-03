import random

print("im going to pick u what number are u on (8 literally a gooner fan)")
print("1. Alright")
print("2. No way")
print("3. Yes")
print("4. hell no")
try:  #copilot told me to do ts shi ;-;
    idk = int(input("just pick above the number here: "))
    if idk >= 5:
        print("just pick (1-4) bud")
        exit()
except ValueError:
    print("it supposed to be numbers not letters duh")
    exit()

Random_Numbers = random.randrange(1, 10)
print("your number is: ", Random_Numbers)
if Random_Numbers == 8:
    print("you are a gooner.")
else:
    print("You are safe this time.")
