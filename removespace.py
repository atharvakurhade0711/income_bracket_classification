with open('adult.data', 'r') as f:
    lines = f.readlines()

# remove spaces
lines = [line.replace(' ', '') for line in lines]

# finally, write lines in the file
with open('adult.data', 'w') as f:
    f.writelines(lines)
