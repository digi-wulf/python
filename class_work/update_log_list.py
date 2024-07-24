def update_log_list(log_list):
    for log in log_list:
        for key in log.items():
            if 'database' in log.values():
                log['timestamp'] = '2023-12-07T12:30:00'
            if 'webserver' in log.values():
                log['level'] = 'ERROR'

    return log_list

log_sample = [
    {"app": "webserver", "level": "INFO", "message": "Critical error", "timestamp": "2023-12-07T11:55:00"},
    {"app": "database", "level": "ERROR", "message": "Database connection lost", "timestamp": "2023-12-07T11:50:00"}
    ]

print(update_log_list(log_sample))