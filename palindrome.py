n = input()
rev = ''
for i in n:
    rev = i + rev
if n == rev:
    print("Palindrome")
else:
    print("Not a Palindrome")