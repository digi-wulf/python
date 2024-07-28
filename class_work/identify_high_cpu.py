def identify_high_cpu(cpu_list):
    dict_list = dict(enumerate(cpu_list))
    dict_list = dict((k, v) for k, v in dict_list.items() if v > 90)
            
    return list(dict_list.keys())
    

cpu_list = [85.0, 92.5, 88.0, 95.2]
print(identify_high_cpu(cpu_list))
#Expected result: [1, 3]

cpu_list = [91.0, 88.8, 89.5]
print(identify_high_cpu(cpu_list))
#Expected result: [0]

cpu_list = [92.0, 94.5, 88.0, 95.2, 91.5]
print(identify_high_cpu(cpu_list))
#Expected result: [0, 1, 3, 4]

cpu_list = [70.0, 65.5, 68.0, 75.2, 62.5]
print(identify_high_cpu(cpu_list))
#Expected result: []

cpu_list = [100.0, 0.0, 50.0, 90.1, 89.9]
print(identify_high_cpu(cpu_list))
#Expected result: [0, 3]
# help(help)