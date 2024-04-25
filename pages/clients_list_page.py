from base.base_class import Base


class ClientsList(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    client_lkz_inn = {
        "xpath": "//a[@class='link-back' and contains(text(), '3123625054')]",
        "name": "client_lkz_inn"
    }
    client_lke_inn = {
        "xpath": "//a[@class='link-back' and contains(text(), '5178860124')]",
        "name": "client_lkz_inn"
    }
    action_button = {
        "xpath": "(//button[.//span[contains(text(), 'Действия')]])[2]",
        "name": "action_button"
    }
    go_to_account_button = {
        "xpath": "//button[.//span[contains(text(), 'Перейти в ЛК контрагента')]]",
        "name": "go_to_account_button"
    }
    assert_auto_lkz = {
        "reference_xpath": "//h4[@class='title' and text()='Auto LKZ']",
        "reference": "Auto LKZ"
    }
    accept_button = {
        "xpath": "(//button[.//span[text()='Принять']])[2]",
        "name": "accept_button"
    }