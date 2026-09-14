import time

from .health_checker import check_health


def monitor_target(url: str, interval: int = 5):
    while True:
        result = check_health(url)

        print(f"[MONITOR] {result}")

        time.sleep(interval)