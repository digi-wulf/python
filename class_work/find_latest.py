from datetime import datetime

def find_latest(submissions):
    # Specify date format
    date_format = '%m/%d/%Y %I:%M %p'
    
    # Convert string values to datetime objects.
    submissions.sort(key=lambda date: datetime.strptime(date, date_format))
    for date in submissions:
        new_format = datetime.strptime(date, date_format)
    
    # Determine and return latest
    return new_format


submission_timestamps = ['12/15/2023 08:45 AM', '12/14/2023 03:30 PM', '12/16/2023 11:20 AM', '12/13/2023 06:15 PM']
print(find_latest(submission_timestamps))