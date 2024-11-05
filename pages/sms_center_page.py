import re
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class SmsCenter(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.sms_url = 'https://cp.redsms.ru/'

    # Locators
    sms_login_input = {
        "xpath": "//*[@id='authLoginInput']",
        "name": "sms_login_input"
    }
    sms_password_input = {
        "xpath": "//*[@id='authPasswordInput']",
        "name": "sms_password_input"
    }
    sms_login_button = {
        "xpath": "//button[.//span[text()='Войти']]",
        "name": "sms_login_button"
    }
    detailing_button = {
        "xpath": "//div[text()='Детализация']",
        "name": "detailing_button"
    }
    refresh_button = {
        "xpath": "//button[@class='TlYSdkvjy8CvSMMQ0Zfb RkndBZDErw_QNC9G8r72 HStWRKScOyQNFQYvXccg Vd5x6c7IiEaFl4pAvotC Sp_9XlfPRQdlk8xOYoyU']",
        "name": "refresh_button"
    }

    """ Get sms code with retries """
    def get_confirmation_code(self, phone_number, max_attempts=12):
        """
        Извлекает код подтверждения, связанный с заданным номером телефона, с повторными попытками.

        Parameters
        ----------
        phone_number : str
            Номер телефона в формате 10 цифр без префикса.
        max_attempts : int, optional
            Максимальное количество попыток проверки.

        Returns
        -------
        str or None
            Код подтверждения как строку, если найден, или None, если не найден после всех попыток.

        Raises
        ------
        ValueError
            Если код подтверждения не найден после всех попыток.
        """
        formatted_phone = '+7' + phone_number
        xpath_locator = f"//tr[contains(.//div, '{formatted_phone}')]//div[contains(text(), 'Код подтверждения:')]"
        
        for attempt in range(max_attempts):
            try:
                element_text = WebDriverWait(self.driver, 5).until(
                    EC.visibility_of_element_located((By.XPATH, xpath_locator))
                ).text
                match = re.search(r'\d+', element_text)
                if match:
                    print(f"Код подтверждения получен на попытке {attempt + 1}: {match.group(0)}")
                    return match.group(0)
            except TimeoutException:
                print(f"Попытка {attempt + 1} не удалась. Обновляем страницу...")
                self.click_button(self.refresh_button)
        
        # Если после всех попыток код не найден, выбрасываем ошибку
        raise ValueError(f"Код подтверждения для номера {formatted_phone} не найден после {max_attempts} попыток.")
