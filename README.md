# WebSoket通信のサーバ、クライアントの実装例

## 実行環境

Python 3.10.11

## 環境構築

```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

## 動作確認

* 以降のコマンドは仮想環境をアクティベートした前提で進めます。

```bash
.\venv\Scripts\activate
```

### サーバ

```bash
python server.py
```

* logフォルダにファイルが追加されると接続中のクライアントに新しいファイル名を通知します。

### クライアント

* 複数のクライアントからサーバに接続可能です。
* 複数接続する場合は異なるコンソールでクライアントを実行してください。

```bash
python client.py
```
