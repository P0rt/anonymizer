import re
import json

def anonymize_data(data):
    # Replacing email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}'
    data = re.sub(email_pattern, '[EMAIL_ID]', data)

    # Replacing URLs
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    data = re.sub(url_pattern, '[URL_ID]', data)

    # Replacing mentions
    mention_pattern = r'@[\w]+'
    data = re.sub(mention_pattern, '[MENTION_ID]', data)

    return data

# Data
with open("data/sample.json", "r", encoding="utf-8") as file:
    data_dict = json.load(file)

anonymized_data = {key: [anonymize_data(item) if isinstance(item, str) else item for item in value] for key, value in data_dict.items()}

# Output
with open("anon/result.json", "w", encoding="utf-8") as outfile:
    json.dump(anonymized_data, outfile, indent=2, ensure_ascii=False)
