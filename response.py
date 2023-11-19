import pickle
import os
from dotenv import load_dotenv

from web_scrape import fetch_website_content, get_internal_links, scrape_all_pages


from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback
from langchain.chat_models import ChatOpenAI



def get_response(query, VectorStoreFile):

    load_dotenv()

    VectorStore = pickle.load(open(VectorStoreFile, "rb"))
    
    docs = VectorStore.similarity_search(query, k=3) ## k = number of results - top 3

    llm = ChatOpenAI(
        model_name="gpt-3.5-turbo", 
        temperature=0)

    
    chain = load_qa_chain(llm=llm, chain_type="stuff")
    
    with get_openai_callback() as callback:
        response = chain.run(input_documents=docs, question=query)
    return response     ## kan returnere callback her ogsså, for å få mer info om kostnader og tokens tilknyttet svaret


#text = get_response("Hva er coax?", "COAX_web_content.pkl")
#print(text)
#embedd_text(text)