from base.base_class import Base


class TransportAdd(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    """Transport types drop-down list"""
    vehicle_type_select = {
        "xpath": "//*[@id='main']/div/div[3]/div[2]/div/div[2]/div/div/div/div/div/label/div/div[1]/div/div/div",
        "name": "vehicle_type_select"
    }
    vehicle_owner_select = {
        "xpath": "//div[@class='ant-input flexbox ']",
        "name": "vehicle_owner_select"
    }
    plate_number_input = {
        "xpath": "//input[@name='plateNumber']",
        "name": "plate_number_input"
    }
    mark_model_input = {
        "xpath": "//input[@name='markAndModel']",
        "name": "mark_model_input"
    }
    """Owner types drop-down list"""
    owner_types_select = {
        "xpath": "//span[contains(text(), 'Собственник')]",
        "name": "owner_types_select"
    }
    """Year of issue drop-down list"""
    year_select = {
        "xpath": "//span[contains(text(), 'Год Выпуска')]",
        "name": "year_select"
    }
    """Vehicle categories drop-down list"""
    vehicle_categories_select = {
        "xpath": "//span[contains(text(), 'Тип автоперевозки')]",
        "name": "vehicle_categories_select"
    }
    """Vehicle body types drop-down list"""
    vehicle_body_types_select = {
        "xpath": "//span[contains(text(), 'Подходящие типы кузова')]",
        "name": "vehicle_body_types_select"
    }
    capacity_input = {
        "xpath": "//input[@name='liftingCapacityInKg']",
        "name": "capacity_input"
    }
    volume_input = {
        "xpath": "//input[@name='volume']",
        "name": "volume_input"
    }
    pallets_input = {
        "xpath": "//input[@name='palletsCapacity']",
        "name": "pallets_input"
    }
    height_from_ground_input = {
        "xpath": "//input[@name='heightFromGroundInCm']",
        "name": "height_from_ground_input"
    }
    crane_capacity_input = {
        "xpath": "//input[@name='craneCapacity']",
        "name": "crane_capacity_input"
    }
    crane_length_input = {
        "xpath": "//input[@name='craneLength']",
        "name": "crane_length_input"
    }
    compartment_count_input = {
        "xpath": "//input[@name='compartmentCount']",
        "name": "compartment_count_input"
    }
    car_count_input = {
        "xpath": "//input[@name='carCount']",
        "name": "car_count_input"
    }
    create_vehicle_button = {
        "xpath": "//button[contains(@class, 'ant-btn-primary') and .//span[text()='Создать ТС']]",
        "name": "create_vehicle_button",
        "reference_xpath": "//span[@class='ant-modal-confirm-title' and contains(text(), 'успешно создан')]",
        "reference": ".* успешно создан.*"
    }
    edit_confirm_button = {
        "xpath": "//button[contains(@class, 'ant-btn-primary') and .//span[text()='Сохранить']]",
        "name": "edit_confirm_vehicle_button",
        "reference_xpath": "//span[contains(text(), 'успешно обновлен')]",
        "reference": ".* успешно обновлен.*"
    }
    confirm_button = {
        "xpath": "//button[@class='ant-btn ant-btn-primary']",
        "name": "confirm_button"
    }
    yes_button = {
        "xpath": "//button[.//span[text()='Да']]",
        "name": "yes_button"
    }
    ok_button = {
        "xpath": "//button[.//span[text()='OK']]",
        "name": "ok_button",
        "reference_xpath": "//span[text()='OK']",
        "reference": "OK"
    }
    number_passengers_select = {
        "xpath": "//span[contains(text(), 'Пассажиров (без учета водителя)')]",
        "name": "number_passengers_select"
    }
    platform_height_input = {
        "xpath": "//input[@name='platformHeight']",
        "name": "platform_height_input"
    }
    platform_length_input = {
        "xpath": "//input[@name='platformLength']",
        "name": "platform_length_input"
    }
    edit_button = {
        "xpath": "//button[contains(text(), 'Редактировать')]",
        "name": "edit_button"
    }
    hydro_lift_toggl = {
        "xpath": "//span[contains(text(), 'Наличие гидроборта')]",
        "name": "hydro_lift_toggl"
    }
    gps_monitoring_toggl = {
        "xpath": "//span[contains(text(), 'Наличие GPS датчика')]",
        "name": "gps_monitoring_toggl"
    }
    pallets_jack_toggl = {
        "xpath": "//span[contains(text(), 'Наличие рохлы')]",
        "name": "hydro_lift_toggl"
    }
    conics_toggl = {
        "xpath": "//span[contains(text(), 'Наличие коников')]",
        "name": "conics_toggl"
    }
    strap_toggl = {
        "xpath": "//span[contains(text(), 'Наличие ремней')]",
        "name": "strap_toggl"
    }
    chain_toggl = {
        "xpath": "//span[contains(text(), 'Наличие цепи')]",
        "name": "chain_toggl"
    }
    tarpaulin_toggl = {
        "xpath": "//span[contains(text(), 'Наличие брезента')]",
        "name": "tarpaulin_toggl"
    }
    net_toggl = {
        "xpath": "//span[contains(text(), 'Наличие сети')]",
        "name": "net_toggl"
    }
    wheel_chock_toggl = {
        "xpath": "//span[contains(text(), 'Наличие башмаков')]",
        "name": "wheel_chock_toggl"
    }
    corner_pillar_toggl = {
        "xpath": "//span[contains(text(), 'Наличие угловых стоек')]",
        "name": "corner_pillar_toggl"
    }
    doppel_stock_toggl = {
        "xpath": "//span[contains(text(), 'Наличие допельштока')]",
        "name": "doppel_stock_toggl"
    }
    wooden_floor_toggl = {
        "xpath": "//span[contains(text(), 'Наличие деревянного пола')]",
        "name": "wooden_floor_toggl"
    }
    side_loading_toggl = {
        "xpath": "//span[contains(text(), 'Боковая погрузка')]",
        "name": "side_loading_toggl"
    }
    top_loading_toggl = {
        "xpath": "//span[contains(text(), 'Верхняя погрузка')]",
        "name": "top_loading_toggl"
    }
    covered_body_toggl = {
        "xpath": "//span[contains(text(), 'Крытый кузов')]",
        "name": "covered_body_toggl"
    }
    sanitation_toggl = {
        "xpath": "//span[contains(text(), 'Договор о санитарной обработке')]",
        "name": "sanitation_toggl"
    }
    sanitary_date_button = {
        "xpath": "//input[@name='sanitaryPassportExpiresAtDate']",
        "name": "sanitary_date_button"
    }
    calendar_input = {
        "xpath": "//input[@class='ant-calendar-input ']",
        "name": "calendar_input"
    }
    first_pass_type_select = {
        "xpath": "//label[contains(@class, 'vz-form-item') and .//span[contains(@class, 'vz-form-item__label') and "
                 "contains(text(), 'Тип пропуска')]]//div[contains(@class, 'ant-select-selection__rendered')]",
        "name": "first_pass_type_select"
    }
    second_pass_type_select = {
        "xpath": "(//label[contains(@class, 'vz-form-item') and .//span[contains(@class, 'vz-form-item__label') and "
                 "contains(text(), 'Тип пропуска')]]//div[contains(@class, 'ant-select-selection__rendered')])[2]",
        "name": "second_pass_type_select"
    }
    third_pass_type_select = {
        "xpath": "(//label[contains(@class, 'vz-form-item') and .//span[contains(@class, 'vz-form-item__label') and "
                 "contains(text(), 'Тип пропуска')]]//div[contains(@class, 'ant-select-selection__rendered')])[3]",
        "name": "third_pass_type_select"
    }
    first_pass_date_button = {
        "xpath": "(//input[@class='ant-calendar-picker-input ant-input'])[2]",
        "name": "first_pass_date_button"
    }
    second_pass_date_button = {
        "xpath": "(//input[@class='ant-calendar-picker-input ant-input'])[3]",
        "name": "second_pass_date_button"
    }
    third_pass_date_button = {
        "xpath": "(//input[@class='ant-calendar-picker-input ant-input'])[4]",
        "name": "third_pass_date_button"
    }
    tractor_first_pass_date_button = {
        "xpath": "(//input[@class='ant-calendar-picker-input ant-input'])[1]",
        "name": "tractor_first_pass_date_button"
    }
    tractor_second_pass_date_button = {
        "xpath": "(//input[@class='ant-calendar-picker-input ant-input'])[2]",
        "name": "tractor_second_pass_date_button"
    }
    tractor_third_pass_date_button = {
        "xpath": "(//input[@class='ant-calendar-picker-input ant-input'])[3]",
        "name": "tractor_third_pass_date_button"
    }
    close_circle_button = {
        "xpath": "//i[@aria-label='icon: close-circle']",
        "name": "close_circle_button"
    }
    attach_button = {
        "xpath": "//button[@class='semi-wide element-button theme-primary']",
        "name": "attach_button"
    }
    select_button = {
        "xpath": "//button[@type='button' and contains(@class, 'ant-btn')]",
        "name": "select_button"
    }
    unselect_button = {
        "xpath": "//button[.//img[@alt='xWhite']]",
        "name": "unselect_button"
    }
    assign_selected_button = {
        "xpath": "//button[.//span[text()='Назначить выбранных']]",
        "name": "assign_selected_button"
    }
    action_menu_button = {
        "xpath": "//span[@class='icon-content']",
        "name": "action_menu_button"
    }
    suspend_button = {
        "xpath": "//span[normalize-space()='Временно приостановить']",
        "name": "suspend_button"
    }
    resume_button = {
        "xpath": "//span[normalize-space()='Возобновить']",
        "name": "resume_button"
    }
    exploitation_finish_button = {
        "xpath": "//span[normalize-space()='Эксплуатация завершена']",
        "name": "exploitation_finish_button"
    }

    def all_additional_params_without_gps(self):
        buttons_to_click = [
            self.hydro_lift_toggl,
            self.pallets_jack_toggl,
            self.conics_toggl,
            self.strap_toggl,
            self.chain_toggl,
            self.tarpaulin_toggl,
            self.net_toggl,
            self.wheel_chock_toggl,
            self.corner_pillar_toggl,
            self.doppel_stock_toggl,
            self.wooden_floor_toggl
        ]
        for button in buttons_to_click:
            self.click_button(button)
