import websocket
import _thread
import time
import json
def on_message(ws, message):
    with open("monitor-1.png", 'wb') as f:
        f.write(message)

if __name__ == "__main__":
    ws = websocket.WebSocketApp("ws://127.0.0.1:56537/minicap",
                              on_message=on_message)
    ws.run_forever()