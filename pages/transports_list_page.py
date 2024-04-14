from base.base_class import Base


class TransportsList(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    add_transport_button = {
        "xpath": "//button[@class='filter-button rounded box-shadow primary default']",
        "name": "add_transport_button"
    }
    first_radio_button = {
        "xpath": "(//input[@type='radio' and @class='ant-radio-input'])[3]",
        "name": "first_radio_button"
    }
    confirm_choice_button = {
        "xpath": "//button[@class='ant-btn margin-left-15 ant-btn-primary']",
        "name": "confirm_choice_button"
    }