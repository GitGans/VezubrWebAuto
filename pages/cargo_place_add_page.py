from typing import NoReturn
from base.base_class import Base


class CargoPlaceAdd(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    """Cargo place owner drop-down list"""
    cargo_place_owner_select = {
        "xpath": "//span[@class='vz-form-item__label ' and contains(text(),'Владелец Задания')]",
        "name": "cargo_place_owner_select"
    }
    select_own_cargo_place = {
        "xpath": "//ul[@role='listbox']/li[text()='Собственное Задание Экспедитора']",
        "name": "select_own_cargo_place"
    }
    select_cargo_place_lkz = {
        "xpath": "//ul[@role='listbox']/li[text()='Auto LKZ']",
        "name": "select_cargo_place_lkz"
    }
    """Cargo place owner drop-down list"""
    child_cp_select = {
        "xpath": "//div[@class='vz-form-item__label' and contains(text(), 'Вложенные Задания')]",
        "name": "child_cp_select"
    }
    """Cargo place type drop-down list"""
    lke_cp_type_select = {
        "xpath": "(//div[@class='ant-select-selection__rendered'])[2]",
        "name": "cargo_place_type_select"
    }
    lkz_cp_type_select = {
        "xpath": "(//div[@class='ant-select-selection__rendered'])[1]",
        "name": "cargo_place_type_select"
    }
    cp_quantity_input = {
        "xpath": "(//input[@role='spinbutton'])[1]",
        "name": "cp_quantity_input"
    }
    cp_weight_input = {
        "xpath": "(//input[@role='spinbutton'])[2]",
        "name": "cp_weight_input"
    }
    cp_value_input = {
        "xpath": "(//input[@role='spinbutton'])[3]",
        "name": "cp_value_input"
    }
    cp_cost_input = {
        "xpath": "(//input[@role='spinbutton'])[4]",
        "name": "cp_cost_input"
    }
    """Cargo place status drop-down list"""
    lke_cp_status_select = {
        "xpath": "(//div[@class='ant-select-selection__rendered'])[4]",
        "name": "lke_cp_status_select"
    }
    lkz_cp_status_select = {
        "xpath": "(//div[@class='ant-select-selection__rendered'])[3]",
        "name": "lkz_cp_status_select"
    }
    lkz_cp_title_input = {
        "xpath": "(//input[@type='text'])[2]",
        "name": "lkz_cp_title_input"
    }
    lkz_invoice_number_input = {
        "xpath": "(//input[@type='text'])[3]",
        "name": "lkz_invoice_number_input"
    }
    lke_cp_title_input = {
        "xpath": "(//input[@type='text'])[3]",
        "name": "lke_cp_title_input"
    }
    lke_invoice_number_input = {
        "xpath": "(//input[@type='text'])[4]",
        "name": "lke_invoice_number_input"
    }
    invoice_date_input = {
        "xpath": "//input[@class='ant-calendar-picker-input ant-input']",
        "name": "invoice_date_input"
    }
    date_input = {
        "xpath": "//input[@class='ant-calendar-input ']",
        "name": "date_input"
    }
    lkz_bar_code_input = {
        "xpath": "(//input[@type='text'])[4]",
        "name": "lkz_bar_code_input"
    }
    lkz_seal_number_input = {
        "xpath": "(//input[@type='text'])[5]",
        "name": "lkz_seal_number_input"
    }
    lkz_external_id_input = {
        "xpath": "(//input[@type='text'])[6]",
        "name": "lkz_external_id_input"
    }
    lkz_wms_number_input = {
        "xpath": "(//input[@type='text'])[8]",
        "name": "lkz_wms_number_input"
    }
    lke_bar_code_input = {
        "xpath": "(//input[@type='text'])[5]",
        "name": "lke_bar_code_input"
    }
    lke_seal_number_input = {
        "xpath": "(//input[@type='text'])[6]",
        "name": "lke_seal_number_input"
    }
    lke_external_id_input = {
        "xpath": "(//input[@type='text'])[7]",
        "name": "lke_external_id_input"
    }
    lke_wms_number_input = {
        "xpath": "(//input[@type='text'])[9]",
        "name": "lke_wms_number_input"
    }
    temp_from_input = {
        "xpath": "(//input[@role='spinbutton'])[5]",
        "name": "temp_from_input"
    }
    temp_until_input = {
        "xpath": "(//input[@role='spinbutton'])[6]",
        "name": "temp_until_input"
    }
    lkz_comment_input = {
        "xpath": "(//input[@type='text'])[10]",
        "name": "lkz_comment_input"
    }
    lke_comment_input = {
        "xpath": "(//input[@type='text'])[11]",
        "name": "lke_comment_input"
    }
    """Departure address drop-down list"""
    departure_address_select = {
        "xpath": "//span[@class='vz-form-item__label ' and contains(text(),'Адрес отправления')]",
        "name": "departure_address_select"
    }
    select_dp_address_first = {
        "xpath": "(//li[@class='ant-select-dropdown-menu-item ant-select-dropdown-menu-item-active'])[1]",
        "name": "select_dp_address_first"
    }
    """Delivery address drop-down list"""
    delivery_address_select = {
        "xpath": "//span[@class='vz-form-item__label ' and contains(text(),'Адрес доставки')]",
        "name": "delivery_address_select"
    }
    select_dl_address_first = {
        "xpath": "(//li[@class='ant-select-dropdown-menu-item ant-select-dropdown-menu-item-active'])[1]",
        "name": "select_dl_address_first"
    }
    create_cargo_place_button = {
        "xpath": "//button[@class='ant-btn ant-btn-primary']",
        "name": "create_cargo_place_button",
        "reference_xpath": "//div[@class='ant-modal-confirm-content' and text()='Грузоместо успешно создано']",
        "reference": "Грузоместо успешно создано"
    }
    confirm_add_button = {
        "xpath": "(//button[@class='ant-btn ant-btn-primary'])[2]",
        "name": "create_button"
    }
    delete_button = {
        "xpath": "//button[@class='ant-btn margin-right-5']",
        "name": "delete_button",
        "reference_xpath": "//span[@class='ant-modal-confirm-title']",
        "reference": "Вы точно хотите удалить ГМ.*"
    }
    edit_button = {
        "xpath": "//button[@class='ant-btn ant-btn-primary']",
        "name": "edit_button"
    }
    yes_button = {
        "xpath": "//button[contains(., 'Да')]",
        "name": "yes_button"
    }
    ok_button = {
        "xpath": "//button[contains(., 'OK')]",
        "name": "calendar_ok_button"
    }
    quantity_edit = {
        "xpath": "(//input[@role='spinbutton'])[2]",
        "name": "quantity_edit"
    }
    weight_edit = {
        "xpath": "(//input[@role='spinbutton'])[3]",
        "name": "weight_edit"
    }
    value_edit = {
        "xpath": "(//input[@role='spinbutton'])[4]",
        "name": "value_edit"
    }
    cost_edit = {
        "xpath": "(//input[@role='spinbutton'])[5]",
        "name": "cost_edit"
    }
    temp_from_edit = {
        "xpath": "(//input[@role='spinbutton'])[6]",
        "name": "temp_from_edit"
    }
    temp_until_edit = {
        "xpath": "(//input[@role='spinbutton'])[7]",
        "name": "temp_until_edit"
    }
    lkz_cp_title_edit = {
        "xpath": "(//input[@type='text'])[4]",
        "name": "lkz_cp_title_edit"
    }
    lkz_invoice_number_edit = {
        "xpath": "(//input[@type='text'])[5]",
        "name": "lkz_invoice_number_edit"
    }
    lkz_bar_code_edit = {
        "xpath": "(//input[@type='text'])[6]",
        "name": "lkz_bar_code_edit"
    }
    lkz_seal_number_edit = {
        "xpath": "(//input[@type='text'])[7]",
        "name": "lkz_seal_number_edit"
    }
    lkz_external_id_edit = {
        "xpath": "(//input[@type='text'])[8]",
        "name": "lkz_external_id_edit"
    }
    lkz_wms_number_edit = {
        "xpath": "(//input[@type='text'])[10]",
        "name": "lkz_wms_number_edit"
    }
    lkz_comment_edit = {
        "xpath": "(//input[@type='text'])[12]",
        "name": "lkz_comment_edit"
    }
    lke_cp_title_edit = {
        "xpath": "(//input[@type='text'])[5]",
        "name": "lke_cp_title_edit"
    }
    lke_invoice_number_edit = {
        "xpath": "(//input[@type='text'])[6]",
        "name": "lke_invoice_number_edit"
    }
    lke_bar_code_edit = {
        "xpath": "(//input[@type='text'])[7]",
        "name": "lke_bar_code_edit"
    }
    lke_seal_number_edit = {
        "xpath": "(//input[@type='text'])[8]",
        "name": "lke_seal_number_edit"
    }
    lke_external_id_edit = {
        "xpath": "(//input[@type='text'])[9]",
        "name": "lke_external_id_edit"
    }
    lke_wms_number_edit = {
        "xpath": "(//input[@type='text'])[11]",
        "name": "lke_wms_number_edit"
    }
    lke_comment_edit = {
        "xpath": "(//input[@type='text'])[13]",
        "name": "lke_comment_edit"
    }
    save_button = {
        "xpath": "//button[contains(., 'Сохранить')]",
        "name": "save_button"
    }
    # Methods
    """ Create base cargo place"""
    def add_base_cargo_place(self) -> NoReturn:
        """
        Автоматизирует добавление грузоместа  в систему, заполняя поля и выбирая опции из выпадающих списков.
        Процесс включает выбор типа места груза, ввод веса, объема и стоимости груза, выбор статуса,
        указание адресов отправления и доставки, а затем подтверждение создания грузоместа.

        Parameters
        ----------
        Нет входных параметров. Все необходимые данные генерируются или выбираются внутри метода.

        Returns
        -------
        NoReturn
            Ничего не возвращает. Побочные эффекты: изменения на веб-странице.
        """
        # Выбор типа грузоместа
        self.dropdown_click_input_click(self.lkz_cp_type_select, "Короб")
        # Ввод рандомизированных данных для веса, объема и стоимости груза
        self.input_in_field(self.cp_weight_input, self.random_value_float_str(10, 20000))
        self.input_in_field(self.cp_value_input, self.random_value_float_str(0.1, 35.0))
        self.input_in_field(self.cp_cost_input, self.random_value_float_str(100, 1000000))
        # Выбор статуса грузоместа
        self.dropdown_click_input_click(self.lkz_cp_status_select, "Новое")
        # Ввод адресов отправления и доставки
        self.dropdown_click_input_wait_enter(self.departure_address_select, "Екатеринбург")
        self.dropdown_click_input_wait_enter(self.delivery_address_select, "Екатеринбург")
        # Последовательное нажатие на кнопки с условиями
        buttons_to_click = [
            {'button': self.create_cargo_place_button, 'do_assert': True, 'wait': None},
            {'button': self.confirm_add_button, 'do_assert': False, 'wait': "lst"}
        ]
        for button_info in buttons_to_click:
            self.click_button(button_info['button'], do_assert=button_info.get('do_assert', False),
                              wait=button_info.get('wait', None))
            