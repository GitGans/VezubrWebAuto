from base.base_class import Base


class User(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    surname_input = {
        "xpath": "//input[@id='surname']",
        "name": "surname_input"
    }
    name_input = {
        "xpath": "//input[@id='name']",
        "name": "name_input"
    }
    patronymic_input = {
        "xpath": "//input[@id='patronymic']",
        "name": "patronymic_input"
    }
    """User type drop-down list"""
    user_type_select = {
        "xpath": "//span[text()='Тип пользователя']",
        "name": "user_type_select"
    }
    """User role drop-down list"""
    user_role_select = {
        "xpath": "//span[text()='Роль пользователя']",
        "name": "user_role_select"
    }
    user_role_reset = {
        "xpath": "//i[@class='anticon anticon-close ant-select-remove-icon']",
        "name": "user_role_reset"
    }
    phone_input = {
        "xpath": "//input[@id='phone']",
        "name": "phone_input"
    }
    email_input = {
        "xpath": "//input[@id='email']",
        "name": "email_input"
    }
    """User timezone drop-down list"""
    user_timezone_select = {
        "xpath": "//span[text()='Часовой пояс']",
        "name": "user_timezone_select"
    }
    """User subdivision drop-down list"""
    user_subdivision_select = {
        "xpath": "//span[text()='Подразделение']",
        "name": "user_subdivision_select"
    }
    """User subdivision drop-down list"""
    user_group_select = {
        "xpath": "//span[text()='Группы']",
        "name": "user_subdivision_select"
    }
    create_user_button = {
        "xpath": "//button[@class='ant-btn semi-wide margin-left-16 ant-btn-primary']",
        "name": "create_user_button",
        "reference_xpath": "//div[@class='ant-modal-confirm-content' and text()='Пользователь создан. На указанный email отправлено письмо с информацией о Логине и Пароле для входа в Ваш ЛК Vezubr']",
        "reference": "Пользователь создан. На указанный email отправлено письмо с информацией о Логине и Пароле для входа в Ваш ЛК Vezubr"
    }
    save_edit_user_button = {
        "xpath": "//button[@class='ant-btn semi-wide margin-left-16 ant-btn-primary']",
        "name": "save_edit_user_button",
        "reference_xpath": "//div[@class='ant-modal-confirm-content' and text()='Данные пользователя успешно изменены']",
        "reference": "Данные пользователя успешно изменены"
    }
    user_edit_button = {
        "xpath": "//button[contains(@class, 'ant-btn-primary') and contains(., 'Редактировать')]",
        "name": "user_edit_button"
    }
    confirm_add_button = {
        "xpath": "//button[@class='ant-btn ant-btn-primary']",
        "name": "create_button"
    }
    add_responsible_button = {
        "xpath": "//button[@class='filter-button rounded box-shadow primary default']",
        "name": "add_responsible_button"
    }
    producer_tab = {
        "xpath": "//a[contains(text(),'Подрядчики')]",
        "name": "producer_tab"
    }
    """Assign responsibility list"""
    all_client_on_checkbox = {
        "xpath": "(//span[@class='ant-checkbox'])[4]",
        "name": "all_client_on_checkbox"
    }
    all_producer_on_checkbox = {
        "xpath": "(//span[@class='ant-checkbox'])[6]",
        "name": "all_producer_on_checkbox"
    }
    all_contractor_off_checkbox = {
        "xpath": "//span[@class='ant-checkbox']",
        "name": "all_contractor_off_checkbox"
    }
    """Contractor role drop-down list"""
    contractor_role_select = {
        "xpath": "(//div[@class='ant-select-selection__rendered'])[6]",
        "name": "contractor_role_select"
    }
    select_producer = {
        "xpath": "//li[@title='Подрядчик']",
        "name": "select_producer"
    }
    select_client = {
        "xpath": "//li[@title='Грузовладелец']",
        "name": "select_client"
    }
    confirm_responsible_button = {
        "xpath": "(//button[@class='ant-btn'])[4]",
        "name": "confirm_responsible_button"
    }
    off_responsibility_button = {
        "xpath": "//button[span[contains(text(), 'Отвязать контрагентов')]]",
        "name": "off_responsibility_button"
    }
    delegate_responsibility_button = {
        "xpath": "//button[span[contains(text(), 'Делегировать Пользователям')]]",
        "name": "delegate_responsibility_button"
    }
    user_checkbox = {
        "xpath": "//span[@class='ant-checkbox']",
        "name": "user_checkbox_empty"
    }
    confirm_off_responsible_button = {
        "xpath": "//button[@class='ant-btn ant-btn-primary']",
        "name": "confirm_off_responsible_button",
        "reference_xpath": "//h2[@class='big-title title-bold']",
        "reference": "Ответственный за Контрагентов"
    }