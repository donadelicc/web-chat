import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def askGPT(nettside, prompt):
    messages = [
        {"role": "system", "content": 
         """
        Du er en hjelpsom assisten som har som eneste oppgave å besvare alle mulige spørsmål som du blir spurt om
        angående en spesifikk nettside. Alt innhold på nettsiden finner du i denne teksten: """ + nettside + """
        Du skal kun svare på spørsmål som er relevant for nettsiden.
        Alle andre spørsmål skal besvares med denne setningen: "Nettsiden har ingen informasjon om dette". 
         """
        },
            {"role": "user", "content": f"{prompt}"
            },
        ]
    response = openai.ChatCompletion.create(
        messages=messages,
        model="gpt-3.5-turbo",
        max_tokens=300,
        temperature=0.1,
    )
    return response['choices'][0]['message']['content']


