import logging
from flask import Flask, request, jsonify

from operator import itemgetter
from langchain.memory import ConversationBufferWindowMemory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_openai import ChatOpenAI

import requests
from config import OLLAMA_BASE_URL, OLLAMA_MODEL, OLLAMA_API_KEY

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# (default: mistral:instruct)
model = ChatOpenAI(
    temperature=0,
    model_name=OLLAMA_MODEL,
    openai_api_base=OLLAMA_BASE_URL,
    openai_api_key=OLLAMA_API_KEY,
    max_tokens=80,
)

# define the prompt and system message
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You're Siri-GPT, an open source AI smarter than Siri that runs on user's devices. You're helping a user with tasks, for any question answer very briefly (answer is about 30 words) and informatively. else, ask for more information.",
        ),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}"),
    ]
)


# define memory type
memory = ConversationBufferWindowMemory(k=5, return_messages=True)

# define the chain
chain = (
    RunnablePassthrough.assign(
        history=RunnableLambda(memory.load_memory_variables) | itemgetter("history")
    )
    | prompt
    | model
)


def generate(user_input: str = "") -> str:
    logging.info(f'Current memory: {memory.load_memory_variables({})}')
    if not user_input:
        return "End of conversation"
    try:
        inputs = {"input": user_input}
        response = chain.invoke(inputs)
        memory.save_context(inputs, {"output": response.content})
        return response.content
    except Exception as e:
        logging.error(f"Error during LLM generation: {e}")
        return "An error occurred while generating the response."


@app.route("/", methods=["POST"])
def generate_route():
    if not request.json or "prompt" not in request.json:
        logging.warning("Bad request: 'prompt' missing from JSON payload.")
        return jsonify({"error": "Bad Request: 'prompt' field is required."}), 400
    
    user_prompt = request.json.get("prompt", "")
    logging.info(f"Received prompt: {user_prompt}")
    
    response_content = generate(user_prompt)
    
    if "An error occurred" in response_content:
        return jsonify({"error": response_content}), 500
    
    return jsonify({"response": response_content})


if __name__ == "__main__":
    app.run(host="0.0.0.0")
