# Study LangChain Chatbot

このプロジェクトは、LangChain と OpenAI の GPT モデルを使用して、Python ソースコードを理解して議論できる AI チャットボットを実装します。チャットボットは、オプションの認証を備えた Gradio Web インターフェースを通じて提供されます。

## 実行手順

### 1. Python のバージョンの確認

以下のコマンドで、Poetry で実行できる Python のバージョンが　[.tool-verisons](.tool-versions) 　に書かれたバージョンと一致しているか確認してください。

```console
poetry run python --version
```

> **Note**
> もしも想定外のバージョンが表示された場合、以下の手順を試してください。
>
> - `poetry env list` コマンドで、poetry で作成した環境を表示
> - `poetry env remove 3.10` などのコマンドで環境を一通り削除
> - `poetry env use $(which python)` コマンドを実行

### 2. パッケージのインストール

```console
make init
```

### 3. `.env` ファイルの作成

以下のような内容で、`.env` ファイルを作成してください。

```
OPENAI_API_KEY=<your-openai-api-key>
GRADIO_USERNAME=oshima
GRADIO_PASSWORD=oshimapassword
APP_ENV=local
```

### 4. 実行

Gradio の Web アプリケーションを起動する

```console
make run
```
