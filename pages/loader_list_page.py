from base.base_class import Base


class LoaderList(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    add_loader_button = {
        "xpath": "//button[@class='filter-button rounded box-shadow primary default']",
        "name": "add_loader_button"
    }
    first_loader_link = {
        "xpath": "//a[@class='link-back']",
        "name": "first_loader_link"
    }
    surname_filter = {
        "xpath": "//input[@placeholder='Фамилия' and @class='ant-input']",
        "name": "surname_filter"
    }
    