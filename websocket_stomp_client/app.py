"""
This module is a websocket client with stomp protocol.
"""
import websocket
import stomper

DEST="/topic/greetings"

if __name__ == "__main__":
    URI = "ws://localhost:8080/hello"
    websocket.enableTrace(True)
    ws = websocket.create_connection(URI)
    print(ws)

    print("create sub protocol")
    sub = stomper.subscribe(DEST,2,ack='auto')
    print(sub)
    print("send protocol")
    ws.send(sub)
    while True:
        result = ws.recv()
        print(result)
        

    ws.close()
    
    