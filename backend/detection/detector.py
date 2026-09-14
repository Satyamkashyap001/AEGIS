def detect_failure(health_result: dict) -> dict:
    if health_result.get("healthy") is True:
        return {
            "failure_detected": False,
            "reason": None,
        }

    return {
        "failure_detected": True,
        "reason": "Target application health check failed",
    }