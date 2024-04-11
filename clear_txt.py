import sys

# Save the original stdout
original_stdout = sys.stdout

# Redirect stdout to a file
with open('history.txt', 'w') as f:
    sys.stdout = f
