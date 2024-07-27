# Write your code here.
def validate_id(department_id):
    department = 0
    id_num = 0
    for char in department_id[0:3]:
        if (char.isupper()) == True:
            department += 1
        else:
            return False
    for char in department_id[3:]:
        if (char.isnumeric()) == True:
            id_num += 1
        else:
            return False
    
    if len(department_id) > 8 or len(department_id) < 8:
        return False
    elif department > 3 or department < 3:
        return False
    elif id_num > 5 or id_num < 5:
        return False
    else:
        return True
        

# You may alter the code below to test your solution or print help documentation.
# Only the validate_id function will be graded for this assessment.

#print(validate_id("HRD00123"))
#print(validate_id("Ops123456"))
# help(help)