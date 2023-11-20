import os
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient, BlobClient
import pickle
from io import BytesIO

from web_scrape import fetch_website_content, get_internal_links, scrape_all_pages


from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS


def embedd_and_store_text(text):

    load_dotenv()

    text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len
    )
    

    ## teksten burde kanskje formateres og forbedres før den blir sendt til en VectorStore
    chunks = text_splitter.split_text(text)

    embeddings = OpenAIEmbeddings()
    VectorStore = FAISS.from_texts(chunks, embedding=embeddings)

    # Ekstraher nødvendige data fra VectorStore
    vectors = VectorStore.get_vectors()   
    metadata = VectorStore.get_metadata() 

    # Konverter VectorStore til en BytesIO-objekt
    
    pkl_bytes = BytesIO()
    pickle.dump({"vectors": vectors, "metadata": metadata}, pkl_bytes)
    pkl_bytes.seek(0)

    # Azure Blob Storage-tilkoblingsdetaljer
    connect_str = os.getenv("AZURE_COAX_CONNECTION_STRING")
    container_name = os.getenv("AZURE_COAX_CONTAINER_NAME")
    blob_name = "COAX_web_content.pkl"

    # Opprett en BlobServiceClient
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)

    # Laste opp til Azure Blob Storage
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    blob_client.upload_blob(pkl_bytes, blob_type="BlockBlob", overwrite=True)


text = scrape_all_pages("https://www.coax.no/") ## få GPT til å lage en ny og mer sammenhengende tekst?
#print(text)
embedd_and_store_text(text)