import json
import random

# Load quotes
with open(".github/quote/naruto-quotes.json", "r", encoding="utf-8") as f:
    quotes = json.load(f)

quote = random.choice(quotes)

new_quote = f'''> "{quote["quote"]}"  
> **— {quote["author"]}**'''

# Read README
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

start = "<!-- QUOTE_START -->"
end = "<!-- QUOTE_END -->"

if start not in readme or end not in readme:
    raise Exception("QUOTE_START or QUOTE_END marker not found in README.md")

before = readme.split(start)[0]
after = readme.split(end)[1]

updated = before + start + "\n\n" + new_quote + "\n\n" + end + after

with open("README.md", "w", encoding="utf-8") as f:
    f.write(updated)

print("README updated successfully!")
