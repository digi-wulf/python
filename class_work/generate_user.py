def generate_users(username_string, num_accounts):
    acct = []
    for i in range(1,num_accounts+1):
        name = f"{username_string}{i}"
        acct.append(name)
        user = set(acct)
    return user

print(generate_users("test_account", 4))