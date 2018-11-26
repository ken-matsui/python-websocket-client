# coding: utf-8

import sys
import websocket
import _thread
import time
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def on_message(ws, message):
    print("Server sent:", message)

def on_error(ws, error):
    print("Internal error:", error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        print("debug: websocket is opened")

        while(True):
            line = sys.stdin.readline()
            if line == "close\n":
                print("ok")
                ws.close()
            # elif line != "":
            #   print("Client sent:", line)
            #   ws.send(line)


    _thread.start_new_thread(run, ())


if __name__ == "__main__":

    param = sys.argv

    url = "wss://stream.binance.com:9443/ws/bnbbtc@depth";

    if len(param) == 2:
        url = param[1]
        print("debug: param[1] is " + param[1])

    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(url,
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()
