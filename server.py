# https://github.com/Pithikos/python-websocket-server
import os
import time
from websocket_server import WebsocketServer
import logging
import glob

class Server():

    def __init__(self, host, port):
        self.server = WebsocketServer(host=host, port=port, loglevel=logging.DEBUG)
        self.log_directory = "./log"
        # ファイルパス
        self.logfiles = []

    def new_client(self, client, server):
        """クライアント接続時に実行

        Args:
            client (_type_): クライアント
            server (_type_): サーバ
        """
        print(f"new client connected and was given id {client['id']}")
        # クライアントにメッセージ送信
        self.server.send_message_to_all("hey all, a new client has joined us")

    def client_left(self, client, server):
        """クライアント切断時に実行

        Args:
            client (_type_): クライアント
            server (_type_): サーバ
        """
        print(f"client({client['id']}) disconnected")
        self.server.send_message_to_all(f"client({client['id']}) disconnected")

    def message_received(self, client, server, message):
        """クライアントからメッセージを受信した際に実行

        Args:
            client (_type_): クライアント
            server (_type_): サーバ
            message (_type_): 受信メッセージ
        """
        print(f"client({client['id']}) said: {message}")
        # クライアントにメッセージ送信
        self.server.send_message_to_all(message)

    def run(self):
        """サーバを起動
        """
        self.server.set_fn_new_client(self.new_client)
        self.server.set_fn_client_left(self.client_left)
        self.server.set_fn_message_received(self.message_received) 
        self.server.run_forever(True)

if __name__ == "__main__":
    HOST = "localhost"
    PORT = 12355
    server = Server(HOST, PORT)
    server.run()
