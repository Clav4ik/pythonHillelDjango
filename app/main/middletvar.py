import time

class RequestInfoTime:
#Middleware add request time in response header
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()

        response = self.get_response(request)

        duration = time.time() - start_time

        # Add the header. Or do other things, my use case is to send a monitoring metric
        response["X-Request-Timing"] = str( int(duration * 1000))+'ms'
        return response
