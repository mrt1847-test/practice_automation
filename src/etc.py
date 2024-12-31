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
        # 이미지 로드
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        screenshot_base64 = element.screenshot_as_base64()
        image_data = base64.b64decode(screenshot_base64)
        img = Image.open(BytesIO(image_data))
        # 숫자 인식
        recognized_text = pytesseract.image_to_string(img, config="--psm 6")

        print(f"인식된 숫자: {recognized_text}")