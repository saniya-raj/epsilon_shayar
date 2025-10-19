import json
import os

# Ensure poems.json is always accessed correctly (same folder as db.py)
DATA_FILE = os.path.join(os.path.dirname(__file__), 'poems.json')

def load_poems():
    """Load all poems from poems.json"""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump([], f, indent=4)
            return []
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []  # Return empty if file corrupted or empty

def save_poem(new_poem):
    """Append a new poem and save to poems.json"""
    poems = load_poems()
    poems.append(new_poem)
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(poems, f, indent=4, ensure_ascii=False)
    print(f"✅ Poem saved successfully: {new_poem['title']}")

