n = int(input()) # Number of rows for the upper part of the diamond

# Upper half of the diamond including the middle row
for i in range(n):
    print(' ' * (n - i - 1), end="")  # Print spaces to center the stars
    print('* ' * (i + 1))  # Print stars with space between them

# Lower half of the diamond (excluding the middle row)
for i in range(n - 1):
    print(' ' * (i + 1), end="")  # Print spaces to center the stars
    print('* ' * (n - i - 1))  # Print stars with space between them