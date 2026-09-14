from datetime import datetime


def create_incident(health_result: dict, detection_result: dict) -> dict:
    return {
        "incident_id": f"INC-{datetime.now().strftime('%Y%m%d%H%M%S')}",
        "status": "OPEN",
        "created_at": datetime.now().isoformat(),
        "url": health_result.get("url"),
        "failure_detected": detection_result.get("failure_detected"),
        "reason": detection_result.get("reason"),
        "evidence": health_result,
    }