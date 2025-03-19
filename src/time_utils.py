import datetime

def is_night_time() -> bool:
    """
    根據當下時間判斷是否為夜間(夜間設定為20:00到隔天06:00)
    """
    now = datetime.datetime.now()
    return now.hour >= 20 or now.hour < 6