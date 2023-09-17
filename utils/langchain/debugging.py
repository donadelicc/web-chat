from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.memory import ConversationBufferWindowMemory
from langchain.memory import ConversationTokenBufferMemory

from langchain.chat_models import ChatOpenAI
import openai
import os
from dotenv import load_dotenv


load_dotenv()
openai.api_key = os.environ['OPENAI_API_KEY']



#memory = ConversationBufferMemory()
#memory = ConversationBufferWindowMemory(k=10) # k is the number of previous messages to remember
#memory = ConversationTokenBufferMemory(max_token_limit=100) # max_token_limit is the maximum number of tokens to rememb

llm = ChatOpenAI(temperature=0.0)
memory = ConversationBufferMemory()
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)
def ask_chain_and_print(question):
    response = conversation.predict(input=question)
    #print(f"You: {question}")
    #print(f"Bot: {response}\n")
    print(response)

# Start samtalen
ask_chain_and_print("Hei, mitt navn er Preben")
ask_chain_and_print("Hva er 1+1?")
ask_chain_and_print("Hva heter jeg?")

#print(dir(conversation))