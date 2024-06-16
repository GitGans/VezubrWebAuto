from base.base_class import Base


class AddressAdd(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    address_input = {
        "xpath": "//*[@id='address_main_form_addressString']/div/div/ul/li/div/input",
        "name": "address_input"
    }
    status_toggl = {
        "xpath": "//button[@id='address_main_form_status']",
        "name": "status_toggl"
    }
    create_address_button = {
        "xpath": "//button[text()='Добавить']",
        "name": "create_address_button",
        "reference_xpath": "//div[@class='ant-modal-confirm-content' and text()='Адрес успешно создан']",
        "reference": "Адрес успешно создан"
    }
    confirm_add_button = {
        "xpath": "//button[@class='ant-btn ant-btn-primary']",
        "name": "create_button"
    }
    