import requests
import os
from bs4 import BeautifulSoup

urls = [
    "https://zakariagoumri.vercel.app/about",
    "https://zakariagoumri.vercel.app/skills",
    "https://zakariagoumri.vercel.app/education",
    "https://zakariagoumri.vercel.app/experience",
    "https://zakariagoumri.vercel.app/contact",
]

os.makedirs("./dataset/portfolio", exist_ok=True)

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text(separator="\n", strip=True)
    route = url.rstrip("/").split("/")[-1]
    fileName = f"./dataset/portfolio/{route}.txt"
    print(f"=== {url} ===")
    with open(fileName, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Saved {url} -> {fileName}")
    print("\n" + "=" * 50 + "\n")
