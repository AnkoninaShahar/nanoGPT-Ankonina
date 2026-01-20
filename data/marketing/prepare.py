import os
import pickle
import json
import numpy as np
import tiktoken
# Load marketing data
with open('data\marketing\marketing_conversations.jsonl', 'r', encoding='utf-8') as f:
    conversations = [json.loads(line) for line in f]
# Choose tokenizer
enc = tiktoken.get_encoding("gpt2")
# Process conversations
train_text = ""
val_text = ""
for i, conv in enumerate(conversations):
    text = ""
    for msg in conv['messages']:
        role = msg['role']
        content = msg['content']
        if role == 'user':
            text += f"User: {content}\n"
        else:
            text += f"Assistant: {content}\n\n"
    
    # Split 90/10
    if i < len(conversations) * 0.9:
        train_text += text
    else:
        val_text += text
# Tokenize
train_ids = enc.encode(train_text)
val_ids = enc.encode(val_text)
# Convert to numpy arrays
train_ids = np.array(train_ids, dtype=np.uint16)
val_ids = np.array(val_ids, dtype=np.uint16)
# Save as binary files
train_ids.tofile('train.bin')
val_ids.tofile('val.bin')
print(f"Train tokens: {len(train_ids)}")
print(f"Val tokens: {len(val_ids)}")
