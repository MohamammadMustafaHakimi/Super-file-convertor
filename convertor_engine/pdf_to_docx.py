# from spire.pdf.common import *
# from spire.pdf import *

# doc = PdfDocument()
# input = "./files/dataMovie.pdf"
# output = "./files/new.docx"

# doc.LoadFromFile(input)

# doc.SaveToFile(output, FileFormat.DOCX)
# doc.Close()
# print("Conversion successful!")

# from pdf2docx import Converter
import os
import subprocess

os.makedirs('generated_docx', exist_ok=True)

# Convert PDF to DOCX
subprocess.run(
    [
        'libreoffice',
        '--headless',
        '--convert-to',
        'docx',
        './files/Keeping your code readable.pdf',
        '--outdir',
        './generated_docx'
    ],
    check=True
)

# Find the generated DOCX file
for filename in os.listdir('generated_docx'):
    if filename.endswith('.docx'):
        input_path = os.path.join('generated_docx', filename)
        break
else:
    raise FileNotFoundError("No DOCX file was generated.")

# Rename to a clean name
os.rename(input_path, 'generated_docx/output.docx')

# def fun(input, output):
#     cv = Converter(input)
#     cv.convert(output, start=0, end=None)
#     cv.close()

# input = "./files/Keeping your code readable.pdf"
# output = "./files/my_data2.docx"
# fun(input, output)
