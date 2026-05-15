def success_response(data=None, message="Success", status=200):
    return {
        "success": True,
        "message": message,
        "data": data
    }


def error_response(message="Error", details=None):
    return {
        "success": False,
        "error": message,
        "details": details
    }
