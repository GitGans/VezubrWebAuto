from base.base_class import Base


class AddressesList(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    add_address_button = {
        "xpath": "//button[@class='filter-button rounded box-shadow primary default']",
        "name": "add_address_button"
    }
    name_filter = {
        "xpath": "//input[@placeholder='Название адреса']",
        "name": "name_filter"
    }
    reset_button = {
        "xpath": "//button[contains(., 'Сбросить')]",
        "name": "reset_button"
    }
    first_address_link = {
        "xpath": "//a[@class='link-back']",
        "name": "first_address_link"
    }
    