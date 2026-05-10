import SimpleServer
import json


# We define a class to handle server requests
class ChatServer:
    def __init__(self):
        """
        We need data to 'persist' between requests. In this case, we want to
        store the history of messages we have received.
        """
        self.history = []

    # This is the server request callback function. You can't change its header.
    def handle_request(self, request):
        """
        A message has just arrived (from the internet)!  We need to respond!
        """
        print(request)
        cmd = request.get_command()
        params = request.get_params()
        if cmd == 'getMsgs':
            return self.get_messages(params)
        if cmd == 'newMsg':
            return self.new_message(params)
        return 'unknown command: ' + cmd

    def get_messages(self, params):
        start_index = int(params['index'])
        # Get items from history at the specified index to the end (using slice)
        to_return = self.history[start_index:]
        # Convert the list to a string, and return the string
        return json.dumps(to_return)

    def new_message(self, params):
        user = params['user']
        msg = params['msg']
        if msg != '':
            self.history.append('[' + user + '] ' + msg)
        return 'success'


def main():
    # Make the server handler
    handler = ChatServer()
    # Start the server to handle internet requests at the specified port
    SimpleServer.run_server(handler, 8000)


if __name__ == '__main__':
    main()
