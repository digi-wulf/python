# Modify this function.
def line_count(filename):
    f = open(filename) 
    contents = f.read()
    lines = contents.split("\n")
    f.close()
    return len(lines)

# You may alter the code below to test your solution or print help documentation.
# Only the line_count function will be graded for this assessment.

print(line_count('TxtFolder\lorem.txt'))
# help(help)