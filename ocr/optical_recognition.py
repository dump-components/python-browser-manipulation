import pytesseract

from system.enviroments import Enviroments

optical_recognition = pytesseract

optical_recognition.pytesseract.tesseract_cmd = Enviroments.path_ocr.value