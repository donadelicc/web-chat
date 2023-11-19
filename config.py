import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("CHATGPT_API_KEY")

if not API_KEY:
    raise ValueError("Please set the CHATGPT_API_KEY environment variable.")