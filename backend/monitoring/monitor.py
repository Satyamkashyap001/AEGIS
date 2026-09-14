import time

from .health_checker import check_health
from ..detection.detector import detect_failure
from ..incident.incident import create_incident
from ..diagnosis.diagnoser import diagnose_failure


def monitor_target(url: str, interval: int = 5):
    while True:
        health_result = check_health(url)
        detection_result = detect_failure(health_result)

        print(f"[MONITOR] {health_result}")
        print(f"[DETECTION] {detection_result}")

        if detection_result["failure_detected"]:
            incident = create_incident(
                health_result,
                detection_result,
            )

            print(f"[INCIDENT] {incident}")

            diagnosis = diagnose_failure(
                health_result,
                detection_result,
            )

            print(f"[DIAGNOSIS] {diagnosis}")

            print("[MONITOR] Failure detected. Stopping monitoring loop.")

            return {
                "health": health_result,
                "detection": detection_result,
                "incident": incident,
                "diagnosis": diagnosis,
            }

        time.sleep(interval)