import os
from PyPDF2 import PdfReader

pdf_path = "/home/zaki/Documents/demarches/mes_documents/myResume.pdf"

output_dir = "./dataset/cv"
os.makedirs(output_dir, exist_ok=True)

reader = PdfReader(pdf_path)
text = ""

for page in reader.pages:
    text += page.extract_text() + "\n"

output_path = os.path.join(output_dir, "cv.txt")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(text)

print(f"Saved extracted CV text to {output_path}")
