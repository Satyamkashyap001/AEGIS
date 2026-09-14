def diagnose_failure(health_result: dict, detection_result: dict) -> dict:
    if not detection_result.get("failure_detected"):
        return {
            "diagnosis_available": False,
            "probable_cause": None,
        }

    error = health_result.get("error", "")

    if error:
        return {
            "diagnosis_available": True,
            "probable_cause": "Target application is unreachable or not running",
            "evidence": error,
        }

    return {
        "diagnosis_available": True,
        "probable_cause": "Target application health check failed",
        "evidence": health_result,
    }