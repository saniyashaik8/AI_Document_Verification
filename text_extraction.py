import pytesseract
from pytesseract import Output
import pandas as pd

# Tell where tesseract.exe is
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_with_confidence(image_array):
    data = pytesseract.image_to_data(image_array, output_type=Output.DATAFRAME)
    data = data[data.conf != -1]
    # Remove NaN
    data = data.dropna(subset=['text'])
    full_text = " ".join(data.text.astype(str))
    avg_conf = data.conf.mean() if not data.empty else 0
    return full_text, data, avg_conf