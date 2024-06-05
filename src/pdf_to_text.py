import os
import pdfplumber
import random
import string

def generate_random_string(length=11):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

folder_path = '../data/pdf'

pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]

for pdf_file in pdf_files:
    pdf = pdfplumber.open(pdf_file)
    page = pdf.pages[0]
    text = page.extract_text().encode('unicode_escape').decode('ascii')
    print(page.extract_text())
    pdf.close()

    f = open(f'../data/text/{generate_random_string()}.txt','w+')   # 使用 w+ 模式開啟 test.txt
    f.write('"')
    f.write(text)               # 寫入內容
    f.write('"')
    f.close()                   # 關閉 test.txt