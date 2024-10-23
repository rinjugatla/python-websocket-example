# https://github.com/Pithikos/python-websocket-server
import os
import time
from websocket_server import WebsocketServer
import logging
import glob

class Server():

    def __init__(self, host, port):
        self.server = WebsocketServer(host=host, port=port, loglevel=logging.DEBUG)
        # 監視するフォルダ
        self.watch_directory = "./log"
        # ファイルパス
        self.watched_files = []
        # 監視間隔
        self.watch_interval_sec = 1

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

    def watch_logfile(self):
        """新規のログがあればクライアントに通知通知
        """
        while True:
            time.sleep(self.watch_interval_sec)
            logfiles = glob.glob(f"{self.watch_directory}/*")
            has_newfile = len(logfiles) > len(self.watched_files)
            if not has_newfile:
                continue

            new_filenames = [os.path.basename(x) for x in logfiles if x not in self.watched_files]
            message = ", ".join(new_filenames)
            self.server.send_message_to_all(message)

            self.watched_files = logfiles

    def run(self):
        """サーバを起動
        """
        self.server.set_fn_new_client(self.new_client)
        self.server.set_fn_client_left(self.client_left)
        self.server.set_fn_message_received(self.message_received) 
        self.server.run_forever(True)
        self.watch_logfile()

if __name__ == "__main__":
    HOST = "localhost"
    PORT = 12355
    server = Server(HOST, PORT)
    server.run()
