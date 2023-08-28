from typing import Any
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
from langchain import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from typing import List
import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ['OPENAI_API_KEY']



def split_text(text: str):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100,
        length_fuction=len
    )
    split_text: list = text_splitter.split(text)
    split_text = [text.replace('\n', ' ') for text in split_text]
    return split_text

model_name = "sentence-transformers/all-mpnet-base-v2"

class Embed:
    def __init__(self):
        self.transformer = SentenceTransformer(model_name)

    def __call__(self, text_batch: List[str]):
        embedding = self.transformer.encode(
            text_batch,
            batch_size=8,
            show_progress_bar=False
        ).tolist()

        return list(zip(text_batch, embedding))

text_and_embedding = []

# Opprett en instans av Embed-klassen.
embedder = Embed()

# Hent embeddings for hver delt tekst.
text_and_embedding = embedder(split_text(text))
