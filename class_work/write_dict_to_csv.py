import csv

def write_dict_to_csv(filename):
    # Data to be written to the CSV file
    fieldnames = ['device_name', 'ip_address']

    data = [
        {'device_name': 'Router1', 'ip_address': '192.168.1.1'},
        {'device_name': 'Router2', 'ip_address': '192.168.1.2'}
    ]

    with open(filename, 'w') as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csvwriter.writeheader()
        csvwriter.writerows(data)
    
    print('\n'.join([','.join(fieldnames)] + [','.join(str(d[field]) for field in fieldnames) for d in data]))
   

write_dict_to_csv('TxtFolder\config.csv')