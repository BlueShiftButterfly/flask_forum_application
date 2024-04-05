from datetime import datetime
from datetime import timezone

def get_utc_timestamp():
    now = int(datetime.now(tz=timezone.utc).timestamp())
    return now

def get_date_from_timestamp(timestamp: int):
    return datetime.fromtimestamp(float(timestamp), tz=timezone.utc)
