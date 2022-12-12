from PIL import Image
from pytesseract import pytesseract
import coordinates

coordinates.photo()

image = Image.open('pasport-test.png')
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.tesseract_cmd = path_to_tesseract
text = pytesseract.image_to_string(image, lang='rus')
print(text)