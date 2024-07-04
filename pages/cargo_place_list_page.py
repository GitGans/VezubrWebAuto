from base.base_class import Base


class CargoPlaceList(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    add_cargo_place_button = {
        "xpath": "//p[@class='no-margin']",
        "name": "add_cargo_place_button"
    }
    cp_list_checkbox = {
        "xpath": "//span[@class='ant-checkbox']",
        "name": "cp_list_checkbox"
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
    first_cp_link = {
        "xpath": "//a[@class='link-back']",
        "name": "first_cp_link"
    }
    barcode_filter = {
        "xpath": "//*[@id='cargoplaces-barcode-filter']",
        "name": "barcode_filter"
    }
    reset_button = {
        "xpath": "//button[contains(., 'Сбросить')]",
        "name": "reset_button"
    }
    action_menu_button = {
        "xpath": "//*[@id='cargoplaces-menu']",
        "name": "action_menu_button"
    }
    multi_select_button = {
        "xpath": "//span[contains(text(), 'Мультивыбор ГМ')]",
        "name": "multi_select_button"
    }
    multi_edit_button = {
        "xpath": "//button[contains(., 'Редактировать')]",
        "name": "multi_edit_button"
    }
    multi_route_button = {
        "xpath": "//button[contains(., 'Маршрутизировать')]",
        "name": "multi_route_button"
    }
    multi_transfer_button = {
        "xpath": "//button[contains(., 'Передать Экспедитору')]",
        "name": "multi_transfer_button"
    }
    vehicle_type_select = {
        "xpath": "//div[@class='ant-select-selection-selected-value' and text()='Добавить машину']",
        "name": "vehicle_type_select"
    }
    quantity_vehicle_input = {
        "xpath": "//input[@placeholder='Кол-во ТС']",
        "name": "quantity_vehicle_input"
    }
    calendar_picker_button = {
        "xpath": "//input[@class='ant-calendar-picker-input ant-input ant-input-sm']",
        "name": "calendar_picker_button"
    }
    today_button = {
        "xpath": "//a[@class='ant-calendar-today-btn ']",
        "name": "today_button"
    }
    calendar_ok_button = {
        "xpath": "//a[@class='ant-calendar-ok-btn']",
        "name": "calendar_ok_button"
    }
    calendar_input = {
        "xpath": "//input[@class='ant-calendar-input ']",
        "name": "today_button"
    }
    send_button = {
        "xpath": "//button[contains(., 'Отправить')]",
        "name": "send_button",
        "reference_xpath": "//div[@class='ant-modal-confirm-content']",
        "reference": "Грузоместа отправлены на маршрутизацию"
    }
    ok_button = {
        "xpath": "//button[@class='ant-btn ant-btn-primary']",
        "name": "ok_button",
        "reference_xpath": "//h2[@class='big-title title-bold']",
        "reference": "Задания"
    }
    field_change_select = {
        "xpath": "(//div[@class='ant-select-selection__rendered'])[5]",
        "name": "field_change_select"
    }
    new_value_select = {
        "xpath": "(//div[@class='ant-select-selection__rendered'])[6]",
        "name": "new_value_select"
    }
    parent_barcode_input = {
        "xpath": "(//input[@type='text' and @class='ant-input'])[11]",
        "name": "parent_barcode_input"
    }
