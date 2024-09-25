from datetime import datetime

def find_latest(submissions):
    # Specify a date format
    date_format = '%m/%d/%Y %I:%M %p'
        
    # Convert string values to datetime objects.
    dt_lst = []
    for date_time in submissions:
        #converted to new format
        new_format = datetime.strptime(date_time, date_format)
        #add to list
        dt_lst.append(new_format)
    #sort the list
    dt_lst.sort(reverse=True)
        
    # Determine and return latest
    return dt_lst[0]


submission_timestamps = ['12/15/2023 08:45 AM', '12/14/2023 03:30 PM', '12/16/2023 11:20 AM', '12/13/2023 06:15 PM']
print("Expected result: 2023-12-16 11:20:00")
print(find_latest(submission_timestamps))
print()

submission_timestamps = ['12/20/2023 02:00 AM', '12/18/2023 10:30 AM', '12/16/2023 07:45 PM', '12/14/2023 04:15 PM']
print("Expected result: 2023-12-20 02:00:00")
print(find_latest(submission_timestamps))
print()

submission_timestamps = ['12/10/2023 11:45 AM', '12/12/2023 05:30 PM', '12/14/2023 08:20 AM', '12/16/2023 01:15 PM']
print("Expected result: 2023-12-16 13:15:00")
print(find_latest(submission_timestamps))
print()

submission_timestamps = ['12/15/2023 08:45 AM', '12/14/2023 03:30 PM', '12/16/2023 11:20 AM', '12/13/2023 06:15 PM']
print("Expected result: 2023-12-16 11:20:00")
print(find_latest(submission_timestamps))
print()

submission_timestamps = ['07/04/1776 12:00 PM', '09/17/1787 03:30 PM', '04/12/1861 04:30 AM', '11/11/1918 11:00 AM', '12/07/1941 07:55 AM', '08/28/1963 03:00 PM', '07/20/1969 08:18 PM', '08/18/1920 04:00 PM', '08/28/1965 02:30 PM', '09/11/2001 08:46 AM', '01/20/2009 12:00 PM', '11/04/2008 11:00 PM', '06/25/1950 04:00 AM', '03/23/2010 08:00 AM', '06/06/1944 06:30 AM']
print("Expected result: 2010-03-23 08:00:00")
print(find_latest(submission_timestamps))
print()