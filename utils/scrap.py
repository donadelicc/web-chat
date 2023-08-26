import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin


def fetch_website_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Kaster en exception hvis responsen er en 4xx eller 5xx feilkode.

        soup = BeautifulSoup(response.text, 'html.parser')

        # Fjern alle <script>, <style>, og <link> tags
        for script in soup(["script", "style", "link"]):
            script.extract()  # fjerner taggen fra soup

        text = soup.get_text()

        cleaned_text = text.replace('\n', ' ')


        return str(cleaned_text)

    except requests.RequestException as e:
        return f"Feil ved henting av nettside: {e}"

def get_internal_links(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        base_url = urlparse(url).scheme + '://' + urlparse(url).netloc
        internal_links = set()
        
        for a_tag in soup.find_all('a', href=True):
            href = a_tag.attrs['href']
            full_url = urljoin(base_url, href)
            if base_url in full_url:  # Dette sjekker om lenken er intern
                internal_links.add(full_url)
        
        return list(internal_links)
    
    except requests.RequestException as e:
        return []

def scrape_all_pages(base_url):
    all_text = ""
    internal_links = get_internal_links(base_url)
    
    for link in internal_links:
        all_text += fetch_website_content(link) + " "
    
    return all_text


def estimate_tokens(text: str) -> int:
    byte_count = len(text.encode('utf-8'))
    return int(byte_count / 4)


#text = scrape_all_pages('https://www.coax.no/')
#estimated_tokens = estimate_tokens(text)
#print(estimated_tokens)


#print(len(scrape_all_pages('https://www.coax.no/')))
#print(len(scrape_all_pages('https://www.coax.no/').split()))



