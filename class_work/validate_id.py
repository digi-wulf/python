# Write your code here.
def validate_id(dep_id):
    department = 0
    id_num = 0
    for char in dep_id[0:3]:
        if (char.isupper()) == True:
            department += 1
        else:
            return False
    for char in dep_id[3:]:
        if (char.isnumeric()) == True:
            id_num += 1
        else:
            return False
    if len(dep_id) == 8 and department == 3 and id_num == 5:
        return True
    else:
        return False
        

# You may alter the code below to test your solution or print help documentation.
# Only the validate_id function will be graded for this assessment.

print(validate_id("HRD00123"))
print(validate_id("Ops123456"))
# help(help)