from base.base_class import Base


class Group(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    title_input = {
        "xpath": "(//input[@class='ant-input'])[1]",
        "name": "title_input"
    }
    """Loader type drop-down list"""
    group_type_select = {
        "xpath": "//div[@class='ant-select-selection__placeholder' and text()='Выберите тип']",
        "name": "group_type_select"
    }
    params_input = {
        "xpath": "(//input[@class='ant-input'])[2]",
        "name": "params_input"
    }
    create_group_button = {
        "xpath": "//button[@class='ant-btn semi-wide margin-left-16 ant-btn-primary']",
        "name": "create_group_button",
        "reference_xpath": "//div[@class='ant-modal-confirm-content' and text()='Группа успешно создана']",
        "reference": "Группа успешно создана"
    }
    confirm_add_button = {
        "xpath": "//button[@class='ant-btn ant-btn-primary']",
        "name": "confirm_button"
    }
