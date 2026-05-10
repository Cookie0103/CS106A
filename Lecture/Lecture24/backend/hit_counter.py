import SimpleServer


# We define a class to handle server requests
class HitCounter:
    def __init__(self):
        self.hits = 0

    # this is the server request callback function. You can't change its header.
    def handle_request(self, request):
        print(request)
        self.hits += 1

        print(self.__dict__)
        return str(self.hits) + ' hits to this server'


def main():
    # Make the server handler
    handler = HitCounter()
    # Start the server to handle internet requests at the specified port
    SimpleServer.run_server(handler, 8000)


if __name__ == '__main__':
    main()
