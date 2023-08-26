from scrap import scrape_all_pages

def estimate_tokens(text: str) -> int:
    byte_count = len(text.encode('utf-8'))
    return int(byte_count / 4)

text = scrape_all_pages('https://www.coax.no/')
#reduced_txt = text[:6000]
estimated_tokens = estimate_tokens(text)
print(estimated_tokens)

print("------------------")
print("------------------")
print("------------------")

print(text)