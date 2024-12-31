from src.base_pages.base import *
import pytesseract
from PIL import Image
import base64
from io import BytesIO

class EtcFunction():
    IMPLICIT_WAIT_TIME = 10
    TIMEOUT = 30

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(self.IMPLICIT_WAIT_TIME)
        self.timeout = self.TIMEOUT

    def analyse_image(self, xpath):
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        # 이미지 로드
        try:
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            screenshot_base64 = element.screenshot_as_base64
            image_data = base64.b64decode(screenshot_base64)
            img = Image.open(BytesIO(image_data))
            img.save("loaded_image.png")  # 디버깅용 저장
            print("이미지 로드 완료")
        except Exception as e:
            print(f"이미지 로드 실패: {e}")

        try:
            recognized_text = pytesseract.image_to_string(img, config="--psm 13")
            print(f"인식된 텍스트: {recognized_text}")
            return recognized_text
        except Exception as e:
            print(f"텍스트 인식 실패: {e}")