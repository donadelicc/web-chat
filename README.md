# Wew Chat Interface for COAX AS

## Et enkelt chatgrensesnitt som gir brukeren muligheten til å stille spørsmål om informasjon som allerede finnes på nettsiden og få svar av gpt-3.5 som nå er blitt ekspert på COAX AS.

### Funksjoner

#### scrape_all_pages


--> bruker BeautifulSoup til å finne alle interne linker som tilhører nettsiden og innhente alle HTML kode før det blir omgjort til
og returnrt som en lang streng. 

#### askGPT

```python
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

```

--> tar inn en nettside og en prompt som parametere der nettsiden er strengen scrape_all_pages() metoden returnere og prompten er 
chat meldingen som brukeren sender inn på nettsiden. Metoden Metoden oppretter en ChatCompletion foreslørsel med gpt-3.5-turbo, sender en melding som inneholder 
en instruks som forteller modellen at den skal svare på det brukeren spør om basert på innholdet på nettsiden.


## Hvordan kjøre programmet lokalt:

1. Klon prosjektet
 `git clone [link til repoet]`
2. Installer avhengigheter
 Naviger til roten av prosjektet ditt å kjør denne kommandoen:
`pip install -r requirements.txt`
4. Kjør applikasjonen
`flask run`





