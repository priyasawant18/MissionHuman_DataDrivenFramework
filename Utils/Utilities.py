from selenium import webdriver
from Config.config import TestData


class Testlinks:
    BASE_URL = "https://app.missionhumane.org/"

class Intantiate:
    driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)