import traceback

from StreamingHandler import StreamingHandler
from StreamingServer import StreamingServer
from weather import city, time, sky, temp

if __name__ == "__main__":
    print(f"Hello {city}!")
    print(f"The time is {time}.")
    print(f"The weather is {sky}.")
    print(f"The temperature is {temp}°F.")

    # Display friendly messages
    if sky == "sunny" and 60 < temp < 80 and ((int(time[-8:-6]) >= 6 and time[-2:] == "AM") or (int(time[-8:-6]) <= 6 and time[-2:] == "PM")):
        print("It's a wonderful day for a walk in the park!")
    elif "rain" in sky.lower():
        print("Stay cozy in doors folks!")

    try:
        # Set up and start the streaming server
        address = ('', 8000)
        server = StreamingServer(address, StreamingHandler)
        print("Serving.")
        server.serve_forever()
    except Exception as e:
        print(traceback.format_exc())
        print(f"Exception occurred: {e}")
    finally:
        print("Done!")
