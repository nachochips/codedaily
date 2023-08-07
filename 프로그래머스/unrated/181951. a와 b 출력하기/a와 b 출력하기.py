import sys

# Redirect standard input to the default stdin (usually the keyboard)
sys.stdin = sys.__stdin__

# Now you can proceed with the rest of your code
a, b = input().split(' ')
a = int(a)
b = int(b)
print("a =", a)
print("b =", b)