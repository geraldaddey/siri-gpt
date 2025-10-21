<div align="center">
    <h1>
        <img src="https://github.com/geraldaddey/siri-gpt/blob/main/assets/icon.png?raw=true" width="200" height="200">
        <br>
    </h1>
    <h3>
        Siri GPT
    </h3>
</div>

## Introduction 
Siri-GPT is an Apple shortcut that provides access to locally running Large Language Models (LLMs) through Siri or the shortcut UI on any Apple device connected to the same network as your host machine. It utilizes Langchain and Ollama.


## Installation
1. Install [Ollama](https://ollama.com/) for your machine. You need to run `ollama serve` in the terminal to start the server.
2. Install Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Create a `.env` file in the root directory of the project with the following content (you can modify the values as needed):
    ```
    OLLAMA_BASE_URL=http://localhost:11434/v1
    OLLAMA_MODEL=mistral:instruct
    OLLAMA_API_KEY=ollama
    ```
4. Run the Flask app on your machine:
    ```bash
    python3 app.py
    ```
    **Note:** For production deployments, it is recommended to use a production-ready WSGI server like Gunicorn or uWSGI instead of `python3 app.py`.
5. On your Apple device, download the shortcut from [here](https://www.icloud.com/shortcuts/ce25a5f98e6345e8896744eb811997aa).
6. Run the shortcut through Siri or the Shortcuts app. The first time you run the shortcut, you will be asked to enter your ip address and the port number.

