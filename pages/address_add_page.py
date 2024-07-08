from base.base_class import Base


class AddressAdd(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    name_address_input = {
        "xpath": "//input[@type='text' and @class='ant-input']",
        "name": "name_address_input"
    }
    address_type_select = {
        "xpath": "//span[contains(text(), 'Тип адреса')]",
        "name": "address_type_select"
    }
    address_status_in_app = {
        "xpath": "//span[contains(text(), 'Настройка статусов адреса в МП')]",
        "name": "address_status_in_app"
    }
    address_status_toggl = {
        "xpath": "//span[contains(text(), 'Статус')]",
        "name": "address_status_toggl"
    }
    address_input = {
        "xpath": "//input[@class='ant-input ant-select-search__field']",
        "name": "address_input"
    }
    owner_inn_input = {
        "xpath": "(//input[@class='ant-input ant-select-search__field'])[2]",
        "name": "owner_inn_input"
    }
    update_address_toggl = {
        "xpath": "//span[contains(text(), 'Скорректировать Фактический Адрес')]",
        "name": "update_address_toggl"
    }
    update_pin_toggl = {
        "xpath": "//span[contains(text(), 'Скорректировать Пин на карте')]",
        "name": "update_pin_toggl"
    }
    external_id_input = {
        "xpath": "(//input[@type='text' and @class='ant-input'])[2]",
        "name": "external_id_input"
    }
    max_height_input = {
        "xpath": "//input[@class='ant-input-number-input']",
        "name": "max_height_input"
    }
    max_capacity_input = {
        "xpath": "(//input[@class='ant-input-number-input'])[2]",
        "name": "max_capacity_input"
    }
    loading_type_select = {
        "xpath": "//span[contains(text(), 'Вид погрузки')]",
        "name": "loading_type_select"
    }
    entry_pass_toggl = {
        "xpath": "//span[contains(text(), 'Пропуск на въезд (Да/Нет)')]",
        "name": "entry_pass_toggl"
    }
    time_arrival_input = {
        "xpath": "(//input[@class='ant-input-number-input'])[3]",
        "name": "time_arrival_input"
    }
    time_departure_input = {
        "xpath": "(//input[@class='ant-input-number-input'])[4]",
        "name": "time_departure_input"
    }
    comment_input = {
        "xpath": "//textarea[@class='ant-input']",
        "name": "comment_input"
    }
    contact_person_input = {
        "xpath": "(//input[@type='text' and @class='ant-input'])[3]",
        "name": "contact_person_input"
    }
    mobile_phone_input = {
        "xpath": "(//input[@type='text' and @class='ant-input'])[4]",
        "name": "mobile_phone_input"
    }
    additional_first_input = {
        "xpath": "(//input[@type='text' and @class='ant-input'])[5]",
        "name": "additional_first_input"
    }
    email_input = {
        "xpath": "(//input[@type='text' and @class='ant-input'])[6]",
        "name": "email_input"
    }
    work_phone_input = {
        "xpath": "(//input[@type='text' and @class='ant-input'])[7]",
        "name": "work_phone_input"
    }
    additional_second_input = {
        "xpath": "(//input[@type='text' and @class='ant-input'])[8]",
        "name": "additional_second_input"
    }
    edit_contact_person_input = {
        "xpath": "(//input[@type='text' and @class='ant-input'])[1]",
        "name": "edit_contact_person_input"
    }
    edit_mobile_phone_input = {
        "xpath": "(//input[@type='text' and @class='ant-input'])[2]",
        "name": "edit_mobile_phone_input"
    }
    edit_additional_first_input = {
        "xpath": "(//input[@type='text' and @class='ant-input'])[3]",
        "name": "edit_additional_first_input"
    }
    edit_email_input = {
        "xpath": "(//input[@type='text' and @class='ant-input'])[4]",
        "name": "edit_email_input"
    }
    edit_work_phone_input = {
        "xpath": "(//input[@type='text' and @class='ant-input'])[5]",
        "name": "edit_work_phone_input"
    }
    edit_additional_second_input = {
        "xpath": "(//input[@type='text' and @class='ant-input'])[6]",
        "name": "edit_additional_second_input"
    }
    create_address_button = {
        "xpath": "//button[.//span[text()='Сохранить']]",
        "name": "create_address_button",
        "reference_xpath": "//div[@class='ant-modal-confirm-content' and text()='Адрес успешно создан']",
        "reference": "Адрес успешно создан"
    }
    confirm_button = {
        "xpath": "//button[.//span[text()='OK']]",
        "name": "create_button"
    }
    delete_button = {
        "xpath": "//button[contains(., 'Удалить')]",
        "name": "delete_button",
        "reference_xpath": "//span[@class='ant-modal-confirm-title' and text()='Адрес удален']",
        "reference": "Адрес удален"
    }
    edit_button = {
        "xpath": "//button[contains(., 'Редакировать')]",
        "name": "edit_button"
    }
    general_tab = {
        "xpath": "//a[@class='vz-tabs-modern__item matched' and contains(text(), 'Общая информация')]",
        "name": "general_tab"
    }
    contacts_tab = {
        "xpath": "//a[@class='vz-tabs-modern__item' and contains(text(), 'Контакты')]",
        "name": "contacts_tab"
    }
    schedule_tab = {
        "xpath": "//a[@class='vz-tabs-modern__item' and contains(text(), 'График приема/работы')]",
        "name": "schedule_tab"
    }
    history_tab = {
        "xpath": "//a[@class='vz-tabs-modern__item' and contains(text(), 'История')]",
        "name": "history_tab"
    }
    