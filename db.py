import json
import os

DATA_FILE = 'poems.json'

def load_poems():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_poem(poem):
    poems = load_poems()
    poems.append(poem)
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(poems, f, indent=4, ensure_ascii=False)
