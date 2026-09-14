import time

from .health_checker import check_health
from ..detection.detector import detect_failure


def monitor_target(url: str, interval: int = 5):
    while True:
        health_result = check_health(url)
        detection_result = detect_failure(health_result)

        print(f"[MONITOR] {health_result}")
        print(f"[DETECTION] {detection_result}")

        if detection_result["failure_detected"]:
            print("[MONITOR] Failure detected. Stopping monitoring loop.")

            return {
                "health": health_result,
                "detection": detection_result,
            }

        time.sleep(interval)