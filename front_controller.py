class FrontController:
    def __init__(self, environ, start_response):
        self.environ = environ
        self.start = response_start

    def __iter__(self):
        status = '200 OK'
        headers = [('Content-type', 'text/plain')]
        self.start(status, headers)
        yield "Hello world\n"
