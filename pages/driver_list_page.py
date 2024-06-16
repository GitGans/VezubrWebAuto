from base.base_class import Base


class DriverList(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    add_driver_button = {
        "xpath": "//button[@class='filter-button rounded box-shadow primary default']",
        "name": "add_driver_button"
    }
    first_driver_link = {
        "xpath": "//a[@class='link-back']",
        "name": "first_driver_link"
    }
    surname_filter = {
        "xpath": "//input[@placeholder='Фамилия' and @class='ant-input']",
        "name": "surname_filter"
    }
    