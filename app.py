from flask import Flask, request, jsonify

from operator import itemgetter
from langchain.memory import ConversationBufferWindowMemory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_openai import ChatOpenAI

import requests

app = Flask(__name__)

# (default: mistral:instruct)
model = ChatOpenAI(
    temperature=0,
    model_name="mistral:instruct",
    openai_api_base="http://localhost:11434/v1",
    openai_api_key="insert your api key  here",
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
