<div align="center">
    <h1>
        <img src="https://github.com/geraldddey/siri-gpt/blob/main/assets/icon.png?raw=true" width="200" height="200">
        <br>
    </h1>
    <h3>
        Siri GPT
    </h3>
</div>

### Author: Gerald Kweku Addey

## Introduction 
Siri-GPT is an Apple shortcut that provides access to locally running Large Language Models (LLMs) through Siri or the shortcut UI on any Apple device connected to the same network as your host machine. It utilizes Langchain and Ollama.


## Installation
1. Install [Ollama](https://ollama.com/) for your machine. You need to run `ollama serve` in the terminal to start the server.
2. Install Langchain and Flask, then run the app:
    ```bash
    pip install --upgrade --quiet  langchain langchain-openai
    pip install flask
    ```
    Run the Flask app on your machine:
    ```bash
    python3 app.py
    ```
3. On your Apple device, download the shortcut from [here](https://www.icloud.com/shortcuts/ce25a5f98e6345e8896744eb811997aa).
4. Run the shortcut through Siri or the shortcut UI. The first time you run the shortcut, you will be asked to enter your ip address and the port number.
