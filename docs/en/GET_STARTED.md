# Study LangChain Chatbot

言語: [日本語](/docs/jp/GET_STARTED.md) | English

This project implements an AI chatbot that can understand and discuss Python source code using LangChain and OpenAI's GPT models. The chatbot is served through a Gradio web interface with optional authentication.

<p align="center">
  <img src="/docs/images/image1.png" width="250" />
  <img src="/docs/images/image2.png" width="250" /> 
</p>

## Setup Instructions

### 1. Check Python Version

Use the following command to verify that the Python version available through Poetry matches the version specified in [.tool-versions](.tool-versions):

```console
poetry run python --version
```

> **Note**
> If an unexpected version is displayed, try the following steps:
>
> - Use `poetry env list` command to display environments created by poetry
> - Remove environments using commands like `poetry env remove 3.10`
> - Execute `poetry env use $(which python)` command

### 2. Install Packages

```console
make init
```

### 3. Create `.env` File

Create a `.env` file with the following content:

```
OPENAI_API_KEY=<your-openai-api-key>
GRADIO_USERNAME=oshima
GRADIO_PASSWORD=oshimapassword
APP_ENV=local
```

### 4. Run

Launch the Gradio web application:

```console
make run
```
