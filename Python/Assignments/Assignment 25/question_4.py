import re

def extract_urls(text):
    pattern = r'https?://\S+|www\.\S+'
    urls = re.findall(pattern, text)
    return urls

text = "Visit https://www.google.com and http://example.com for more info."
print(extract_urls(text))
