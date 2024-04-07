from base.base_class import Base


class CargoPlaceList(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    add_cargo_place_button = {
        "xpath": "//p[@class='no-margin']",
        "name": "attach_cargo_place_button"
    }
    cp_list_checkbox = {
        "xpath": "//span[@class='ant-checkbox']",
        "name": "cp_list_checkbox"
    }
    cp_list_checkbox_1 = {
        "xpath": "(//span[@class='ant-checkbox'])[1]",
        "name": "cp_list_checkbox_1"
    }
    cp_list_checkbox_2 = {
        "xpath": "(//span[@class='ant-checkbox'])[2]",
        "name": "cp_list_checkbox_2"
    }
    cp_list_checkbox_3 = {
        "xpath": "(//span[@class='ant-checkbox'])[3]",
        "name": "cp_list_checkbox_3"
    }
    cp_list_checkbox_4 = {
        "xpath": "(//span[@class='ant-checkbox'])[4]",
        "name": "cp_list_checkbox_4"
    }
    date_hover = {
        "xpath": "//*[@id='cargoplaces-maindate-rangepicker']",
        "name": "date_hover"
    }
    date_clear_button = {
        "xpath": "//i[@class='anticon anticon-close-circle ant-calendar-picker-clear']",
        "name": "date_clear_button"
    }
    confirm_button = {
        "xpath": "//button[@class='ant-btn margin-left-15 ant-btn-primary']",
        "name": "create_button"
    }
