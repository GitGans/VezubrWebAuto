from base.base_class import Base


class AddressAdd(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    address_input = {
        "xpath": "//input[@class='ant-input ant-select-search__field']",
        "name": "address_input"
    }
    address_toggl = {
        "xpath": "//button[@role='switch']",
        "name": "address_toggl"
    }
    create_address_button = {
        "xpath": "//button[.//span[text()='Сохранить']]",
        "name": "create_address_button",
        "reference_xpath": "//div[@class='ant-modal-confirm-content' and text()='Адрес успешно создан']",
        "reference": "Адрес успешно создан"
    }
    confirm_add_button = {
        "xpath": "//button[.//span[text()='OK']]",
        "name": "create_button"
    }
    