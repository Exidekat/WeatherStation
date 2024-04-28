import traceback
from sys import argv

from StreamingHandler import StreamingHandler
from StreamingServer import StreamingServer
from weather import webdata

if __name__ == "__main__":
    print(webdata)
    if len(argv) > 1:
        if argv[1] == "--deploy":
            try:
                # Set up and start the streaming server
                port = 8000
                address = ('', port)
                server = StreamingServer(address, StreamingHandler)
                print(f"Serving on port {port}.")
                server.serve_forever()
            except Exception as e:
                print(traceback.format_exc())
                print(f"Exception occurred: {e}")
            finally:
                print("Done!")
