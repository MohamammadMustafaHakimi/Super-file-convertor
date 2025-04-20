# all convertors
# primary: pdf to word, word to pdf, image to pdf, pdf to image, image to docs, docs to image
# secondary p
from pathlib import Path
from gui.view import *
from convertor_engine.docxtopdf import fun
SCRIPT_DIR = Path(__file__).parent
DATA_FILE = SCRIPT_DIR / "data.json"

# fun("./convertor_engine/files/Movie_Data_Analysis_Project.docx", "../Super-file-convertor/generated_pdfs")
