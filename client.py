# https://github.com/websocket-client/websocket-client
import websocket
import rel

class Client():
    def __init__(self, host, port):
        # ログを詳細に表示する場合はコメントアウト
        # websocket.enableTrace(True)
        self.client = websocket.WebSocketApp(
            f"ws://{host}:{port}",
            on_open=self.on_open,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close)
        
    def on_message(self, ws, message):
        """メッセージ受信時に実行

        Args:
            ws (_type_): WebSocket
            message (_type_): メッセージ
        """
        print(f"message: {message}")

    def on_error(self, ws, error):
        """エラー発生時に実行

        Args:
            ws (_type_): WebSocket
            error (_type_): エラー
        """
        print(f"error: {error}")

    def on_close(self, ws, status_code, message):
        """通信終了時に実行

        Args:
            ws (_type_): WebSocket
            status_code (_type_): ステータス
            message (_type_): メッセージ
        """
        print("closed connection")

    def on_open(self, ws):
        """通信開始時に実行

        Args:
            ws (_type_): WebSocket
        """
        print("opened connection")

    def run(self):
        """クライアントを起動
        """
        self.client.run_forever(dispatcher=rel, reconnect=5)
        rel.signal(2, rel.abort)
        rel.dispatch()

if __name__ == "__main__":
    HOST = "localhost"
    PORT = 12355
    client = Client(HOST, PORT)
    client.run()
