from base.base_class import Base


class TariffsList(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    add_tariff_button = {
        "xpath": "//button[@class='filter-button rounded box-shadow default']",
        "name": "add_tariff_button"
    }
    first_tariff_link = {
        "xpath": "//a[@class='link-back']",
        "name": "first_tariff_link"
    }
    tariff_name_filter = {
        "xpath": "//input[@class='ant-input']",
        "name": "tariff_name_filter"
    }
    