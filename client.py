# https://github.com/websocket-client/websocket-client
import websocket
import rel

def on_message(ws, message):
    """メッセージ受信時に実行

    Args:
        ws (_type_): WebSocket
        message (_type_): メッセージ
    """
    print(f"message: {message}")

def on_error(ws, error):
    """エラー発生時に実行

    Args:
        ws (_type_): WebSocket
        error (_type_): エラー
    """
    print(f"error: {error}")

def on_close(ws, status_code, message):
    """通信終了時に実行

    Args:
        ws (_type_): WebSocket
        status_code (_type_): ステータス
        message (_type_): メッセージ
    """
    print("### closed ###")

def on_open(ws):
    """通信開始時に実行

    Args:
        ws (_type_): WebSocket
    """
    print("Opened connection")

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://127.0.0.1:12355",
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    # Set dispatcher to automatic reconnection, 5 second reconnect delay if connection closed unexpectedly
    ws.run_forever(dispatcher=rel, reconnect=5)
    # Keyboard Interrupt
    rel.signal(2, rel.abort)
    rel.dispatch()
