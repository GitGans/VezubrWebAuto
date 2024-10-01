from typing import NoReturn

from base.base_class import Base
from pages.login import accounts


class Login(Base):
    def __init__(self, driver, domain):
        super().__init__(driver)
        self.driver = driver
        self.url = f'https://enter.vezubr.{domain}/login'

    # Locators
    user_email_input = {
        "xpath": "//input[@type='email']",
        "name": 'user_email_input'
    }
    password_input = {
        "xpath": "//input[@type='password']",
        "name": 'password_input'
    }
    login_button = {
        "xpath": "//button[@class='ant-btn wide ant-btn-primary']",
        "name": 'login_button'
    }
    registration_button = {
        "xpath": "//button[@class='ant-btn wide margin-top-16 ant-btn-secondary']",
        "name": 'registration_button'
    }
    assert_inn = {
        "name": "assert_inn",
        "xpath": "//h4[@class='title']",
        "reference_xpath": "//h4[@class='title']"
    }
    registration_urls = {
        "com": "https://enter.vezubr.com/contour-join?contourCode=DgzHgntfhz",
        "ru": "https://enter.vezubr.ru/contour-join?contourCode=rPswPCnWwL"
    }

    # Methods
    """Authorization"""
    def authorization(self, role: str) -> None:
        """
        Выполняет авторизацию пользователя на основе предоставленной роли.

        Parameters
        ----------
        role : str
            Роль пользователя, используемая для выбора учетных данных из справочника accounts.

        Raises
        ------
        KeyError
            Если указанная роль не найдена в справочнике accounts.
        """
        self.driver.get(self.url)
        self.get_current_url()
        self.driver.maximize_window()
        if role in accounts.keys():
            self.input_in_field(self.user_email_input, accounts[role]["email"], safe=True)
            self.input_in_field(self.password_input, accounts[role]["password"], safe=True)
        else:
            print('Incorrect role')

        self.click_button(self.login_button)

    """ Open login page"""
    def registration_start(self) -> NoReturn:
        """
        Открывает страницу регистрации.

        Действия включают переход на URL регистрации, получение текущего URL и максимизацию окна браузера.
        """
        self.driver.get(self.url)
        self.get_current_url()
        self.driver.maximize_window()

    """ Get registration link"""
    def get_registration_url(self, domain: str) -> str:
        """
        Получает URL регистрации на основе заданного домена.

        Parameters
        ----------
        domain : str
            Домен, для которого требуется получить URL регистрации. Должен быть ключом в словаре self.registration_urls.

        Returns
        -------
        str
            URL регистрации для заданного домена.

        Raises
        ------
        KeyError
            Если домен не найден в словаре self.registration_urls.
        """
        return self.registration_urls[domain]

    """ Open login page via link"""
    def registration_via_link(self, domain: str) -> None:
        """
        Открывает страницу регистрации через ссылку, определенную для заданного домена.

        Parameters
        ----------
        domain : str
            Домен, для которого требуется открыть страницу регистрации.
            Используется для получения URL через метод get_registration_url.

        """
        registration_url = self.get_registration_url(domain)
        self.driver.get(registration_url)
        self.get_current_url()
        self.driver.maximize_window()
