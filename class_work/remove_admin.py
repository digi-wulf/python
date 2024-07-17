def remove_admin(usernames, limit):
    i = 0
    validated = []
    admin_count = 0 
    
    while i < limit:
        val_filter = list(filter(lambda x: not x.startswith('admin'), usernames[:limit]))
        i+=1
    for word in usernames[:limit]:
            if word.startswith('admin'):
                admin_count += 1
        
    validated = val_filter
    validated.append("validated")
    
    return validated, admin_count

usernames = ['FN84', 'adminPD66', 'OP83', 'IT32', 'OP27', 'OP13', 'IT95', 'adminHR73', 'OP12', 'HR31']
print(remove_admin(usernames, 10))

# Expected return 
# (['FN84', 'OP83', 'IT32', 'OP27', 'OP13', 'IT95', 'OP12', 'HR31', 'validated'], 2)

# print(remove_admin(usernames, 3))
# Expected result
# (['FN84', 'OP83', 'validated'], 1)