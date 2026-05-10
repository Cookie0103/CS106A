import SimpleServer


# We define a class to handle server requests
class MyFirstServer:
    def __init__(self):
        pass

    # This is the server request callback function. You can't change its header.
    def handle_request(self, request):
        print(request)
        return 'Happy Monday, wonderful cs106a!!!'


def main():
    # Make the server handler
    handler = MyFirstServer()
    # Start the server to handle internet requests at the specified port
    SimpleServer.run_server(handler, 8000)


if __name__ == '__main__':
    main()
