from base.base_class import Base


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
