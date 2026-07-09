#!/usr/bin/env python3
import os

# Read the file
with open('css/styles.css', 'rb') as f:
    content = f.read()

# Fix the corrupted bytes
# Corrupted hamburger: â˜° → ☰
# Corrupted close: âœ• → ✕
# Corrupted dropdown: â–¼ → ▼
# Corrupted checkmark: âœ¦ → ✓

# Convert to string with UTF-8 interpretation of the corrupted sequences
content_str = content.decode('utf-8', errors='replace')

# Replace corrupted sequences
content_str = content_str.replace("'â˜°'", "'☰'")
content_str = content_str.replace("'âœ•'", "'✕'")
content_str = content_str.replace("'â–¼'", "'▼'")
content_str = content_str.replace('"âœ¦"', '"✓"')
content_str = content_str.replace("'âœ¦'", "'✓'")

# Write back
with open('css/styles.css', 'w', encoding='utf-8') as f:
    f.write(content_str)

print("Fixed!")
