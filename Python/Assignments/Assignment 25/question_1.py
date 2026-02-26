import re

def censor_text(text, forbidden_words):
    pattern = r'\b(' + '|'.join(forbidden_words) + r')\b'
    censored_text = re.sub(pattern, '****', text, flags=re.IGNORECASE)
    return censored_text

text = "This is a bad and ugly example"
forbidden = ["bad", "ugly"]

print(censor_text(text, forbidden))
