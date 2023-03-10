def jwt_response_payload_handler(token, user=None, request=None):
    return {
        "code":2000,
        "data":{'token':token,'username':user.username}
    }
