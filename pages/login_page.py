from base.base_class import Base
from pages.login import accounts


class Login(Base):

    def __init__(self, driver, domain):
        super().__init__(driver)
        self.driver = driver
        self.url = f'https://enter.vezubr.{domain}/login'

    # Locators
    user_email_input = {"xpath": "//input[@type='email']", "name": 'user_email_input'}
    password_input = {"xpath": "//input[@type='password']", "name": 'password_input'}
    login_button = {"xpath": "//button[@class='ant-btn wide ant-btn-primary']", "name": 'login_button'}
    registration_button = {"xpath": "//button[@class='ant-btn wide margin-top-16 ant-btn-secondary']",
                           "name": 'registration_button'}

    # Methods
    def authorization(self, role):
        self.driver.get(self.url)
        self.get_current_url()
        self.driver.maximize_window()
        if role in accounts.keys():
            self.input_in_field(self.user_email_input, accounts[role]["email"], safe=True)
            self.input_in_field(self.password_input, accounts[role]["password"], safe=True)
        else:
            print('Incorrect role')

        self.click_button(self.login_button)
