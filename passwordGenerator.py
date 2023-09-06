import secrets
import string

letters = string.ascii_letters
digits = string.digits
special_chart = string.punctuation
alphabet = letters+digits+special_chart

pwd_length = 20
pwd = ''
for i in range(pwd_length):
  pwd += ''.join(secrets.choice(alphabet))

print(pwd)

while True:
  pwd = ''
  for i in range(pwd_length):
    pwd += ''.join(secrets.choice(alphabet))
  if (any(char in special_chart for char in pwd) and
          sum(char in digits for char in pwd) >= 2):
    break
print(pwd);