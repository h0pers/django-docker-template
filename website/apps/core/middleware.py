from secure import Secure, Preset

secure_headers = Secure.from_preset(Preset.BASIC)


def set_secure_headers(get_response):
    """
    Process requests and return a secure response using "secure" library
    """
    def middleware(request):
        response = get_response(request)
        secure_headers.set_headers(response)
        return response
    return middleware
