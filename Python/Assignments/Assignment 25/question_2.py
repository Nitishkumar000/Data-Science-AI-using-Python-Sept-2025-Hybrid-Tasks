import re

def extract_dates(text):
    pattern = (
        r'\b\d{2}/\d{2}/\d{4}\b|'          
        r'\b\d{2}-\d{2}-\d{4}\b|'          
        r'\b(?:January|February|March|April|May|June|'
        r'July|August|September|October|November|December)\s'
        r'\d{1,2},\s\d{4}\b'               
    )

    dates = re.findall(pattern, text)
    return dates


text = "Meeting on 12/05/2023, Independence Day on 15-08-2024, and event on January 1, 2023."
print(extract_dates(text))
