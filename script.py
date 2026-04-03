import re

with open("wiki_data.txt", "r", encoding="utf-8") as f:
    text = f.read()

# ❌ remove brackets
text = re.sub(r'\[.*?\]|\(.*?\)', '', text)

# ❌ remove English letters
text = re.sub(r'[a-zA-Z]', '', text)

# ❌ remove numbers
text = re.sub(r'\d+', '', text)

# ❌ remove special characters (keep only Telugu)
text = re.sub(r'[^\u0C00-\u0C7F\s]', '', text)

# ❌ remove extra spaces
text = re.sub(r'\s+', ' ', text).strip()

with open("clean_telugu.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("🔥 Pure Telugu dataset ready!")