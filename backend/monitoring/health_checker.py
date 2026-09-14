import httpx


def check_health(url: str) -> dict:
    try:
        response = httpx.get(url, timeout=5.0)

        return {
            "url": url,
            "status_code": response.status_code,
            "healthy": response.status_code == 200,
        }

    except httpx.RequestError as error:
        return {
            "url": url,
            "status_code": None,
            "healthy": False,
            "error": str(error),
        }