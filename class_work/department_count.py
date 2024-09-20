def department_count(entries):
    department_codes = ["HRD", "ENG", "MKT", "FIN", "IT"]
    department_counts = {}
    invalid_count = 0
    
    department_counts = {i:entries.count(i) for i in department_codes if entries.count(i) > 0}
    
    
    for code in entries:
        if code == "TEST":
            pass
        else:
            if code not in department_codes:
                invalid_count += 1

    return department_counts, invalid_count

entries = ['HRD', 'MKT', 'HRD', 'IT', 'ENG', 'HRD', 'TEST', 'HRD', 'TEST', 'HRD', 'HRD', 'TEST', 'IT', 'TEST', 'HRD', 'TEST', 'IT', 'TEST', 'ENG', 'MKT', 'TEST', 'IT', 'IT', 'HRD' 'GUEST']
print(department_count(entries))

# Expected return
# ({'HRD': 7, 'MKT': 2, 'IT': 5, 'ENG': 2}, 1)