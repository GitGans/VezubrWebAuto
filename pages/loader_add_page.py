from base.base_class import Base


class LoaderAdd(Base):
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
    passport_id_input = {
        "xpath": "//input[@id='passportId']",
        "name": "passport_id_input"
    }
    passport_by_input = {
        "xpath": "//input[@id='passportIssuedBy']",
        "name": "passport_by_input"
    }
    passport_code_input = {
        "xpath": "//input[@id='passportUnitCode']",
        "name": "passport_code_input"
    }
    """Date of birth"""
    date_of_birth_input = {
        "xpath": "//*[@id='dateOfBirth']/div/input",
        "name": "date_of_birth_input"
    }
    """Passport issued at date"""
    passport_date_input = {
        "xpath": "//*[@id='passportIssuedAtDate']/div/input",
        "name": "passport_date_input"
    }
    """Loader type drop-down list"""
    loader_type_select = {
        "xpath": "//div[@class='ant-select-selection__rendered']",
        "name": "loader_type_select"
    }
    select_loader = {
        "xpath": "//li[contains(text(), 'Грузчик')]",
        "name": "select_loader"
    }
    select_rigger = {
        "xpath": "//li[contains(text(), 'Такелажник')]",
        "name": "select_rigger"
    }
    select_packer = {
        "xpath": "//li[contains(text(), 'Упаковщик')]",
        "name": "select_packer"
    }
    select_picker = {
        "xpath": "//li[contains(text(), 'Сборщик')]",
        "name": "select_picker"
    }
    select_slinger = {
        "xpath": "//li[contains(text(), 'Стропальщик')]",
        "name": "select_slinger"
    }
    select_forklift_operator = {
        "xpath": "//li[contains(text(), 'Карщик')]",
        "name": "select_forklift_operator"
    }
    select_stacker = {
        "xpath": "//li[contains(text(), 'Штабелерщик')]",
        "name": "select_stacker"
    }
    app_phone_input = {
        "xpath": "//input[@id='applicationPhone']",
        "name": "app_phone_input"
    }
    contact_phone_input = {
        "xpath": "//input[@id='contactPhone']",
        "name": "contact_phone_input"
    }
    reg_address_input = {
        "xpath": "//input[@id='registrationAddress']",
        "name": "reg_address_input"
    }
    fact_address_input = {
        "xpath": "//input[@id='factAddress']",
        "name": "fact_address_input"
    }
    """Sanitary book date"""
    sanitary_book_toggl = {
        "xpath": "//*[@id='hasSanitaryBook']",
        "name": "sanitary_book_toggl"
    }
    create_loader_button = {
        "xpath": "//button[text()='Добавить специалиста']",
        "name": "create_loader_button",
        "reference_xpath": "//span[@class='ant-modal-confirm-title' and text()='Специалист был успешно создан']",
        "reference": "Специалист был успешно создан"
    }
    confirm_add_button = {
        "xpath": "//button[@class='ant-btn ant-btn-primary']",
        "name": "create_button"
    }
    action_menu_button = {
        "xpath": "//span[@class='icon-content']",
        "name": "action_menu_button"
    }
    suspend_work_button = {
        "xpath": "//span[normalize-space()='Приостановить работу']",
        "name": "suspend_button"
    }
    ready_to_work_button = {
        "xpath": "//span[normalize-space()='Готов работать']",
        "name": "ready_to_work_button"
    }
    date_button = {
        "xpath": "//input[@class='ant-calendar-picker-input ant-input']",
        "name": "first_pass_date_button"
    }
    calendar_input = {
        "xpath": "//input[@class='ant-calendar-input ']",
        "name": "calendar_input"
    }
    loader_edit_button = {
        "xpath": "//button[contains(text(), 'Редактировать Профиль')]",
        "name": "loader_edit_button"
    }
    close_circle_button = {
        "xpath": "//i[@aria-label='icon: close-circle']",
        "name": "close_circle_button"
    }
    confirm_edit_button = {
        "xpath": "//button[text()='Сохранить изменения']",
        "name": "confirm_edit_button",
        "reference_xpath": "//span[@class='ant-modal-confirm-title' and text()='Данные специалиста успешно обновлены']",
        "reference": "Данные специалиста успешно обновлены"
    }
    passport_toggl = {
        "xpath": "//*[@id='passportRusResident']",
        "name": "sanitary_book_toggl"
    }
    loader_country_select = {
        "xpath": "//*[@id='country']",
        "name": "loader_country_select"
    }
    loader_city_input = {
        "xpath": "//*[@id='placeOfBirth']",
        "name": "loader_city_input"
    }
    
    # Methods
    def add_base_loader(self) -> str:
        """
        Добавляет информацию о грузчике. Включает заполнение личных данных, идентификационных номеров и адресов,
        а также выбор типа грузчика. Процесс завершается созданием и подтверждением создания записи о грузчике.

        Parameters
        ----------
        Нет входных параметров.

        Returns
        -------
        str
            Сгенерированная фамилия грузчика.
        """
        # Ввод информации о грузчике
        surname = f"Ф-{self.get_timestamp()}"
        self.input_in_field(self.surname_input, surname)
        self.input_in_field(self.name_input, f"И-{self.get_timestamp()}")
        self.input_in_field(self.patronymic_input, f"О-{self.get_timestamp()}")
        self.input_in_field(self.passport_id_input, self.random_value_float_str(1000000000, 9999999999))
        self.input_in_field(self.passport_by_input, "Верховный грузила")
        self.input_in_field(self.passport_code_input, self.random_value_float_str(100000, 999999), click_first=True)
        self.dropdown_click_input_click(self.loader_type_select, "Грузчик")
        self.input_in_field(self.app_phone_input, self.random_value_float_str(8650000000, 8659999999), click_first=True)
        self.input_in_field(self.contact_phone_input, self.random_value_float_str(8650000000, 8659999999),
                            click_first=True)
        self.input_in_field(self.reg_address_input, "Мой адрес – Не дом и не улица")
        self.input_in_field(self.fact_address_input, "Мой адрес – Советский Союз.")
        self.click_button(self.create_loader_button, do_assert=True)
        self.click_button(self.confirm_button, wait="lst")

        return surname
    