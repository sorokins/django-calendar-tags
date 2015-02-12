def format_datetime(dt):
    return dt.strftime('%Y%m%dT%H%M%SZ')

def format_datetime_yahoo(dt):
    return dt.strftime('%Y%m%d%H%M%S')

def format_duration_yahoo(d):
    if d:
        return d.strftime('%H%M')