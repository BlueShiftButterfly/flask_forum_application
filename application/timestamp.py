from datetime import datetime, timezone, timedelta

DEFAULT_TIME_DELTA_HOURS = 3 # Corresponds to Helsinki Finland timezone

def get_utc_timestamp():
    now = int(datetime.now(tz=timezone.utc).timestamp())
    return now

def get_date_from_timestamp(timestamp: int):
    return datetime.fromtimestamp(float(timestamp), tz=timezone.utc)

def get_date_string(timestamp: int) -> str:
    dt = get_date_from_timestamp(timestamp).astimezone(timezone(timedelta(hours=DEFAULT_TIME_DELTA_HOURS)))
    return dt.strftime("%d.%m.%Y, %H:%M")
