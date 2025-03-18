import pytesseract
from config import TESSERACT_CMD, OCR_LANG, OCR_CONFIG

pytesseract.pytesseract.tesseract_cmd = TESSERACT_CMD

def extract_text(image):
    return pytesseract.image_to_string(image, lang=OCR_LANG, config=OCR_CONFIG).strip()