import easyocr


def text_recognition(image):
    reader = easyocr.Reader(["ru", "en"])
    result = reader.readtext(image, detail=0, paragraph=True)
    return result
