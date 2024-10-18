import time
import allure
import pytest
from pages.tariff_ftl_add_page import FTLTariffAdd
from pages.tariffs_list_page import TariffsList


@allure.story("Critical path test")
@allure.feature('Создание тарифов')
@allure.description('ЛКЗ. Тест создания FTL тарифа: тип - Почасовой, округление - Час, название - ПЧ-timestamp, '
                    'ТС - 0.5т, кузов - Закрытый, минималка - Рандом')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_ftl_h_tariff_add_lkz(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к списку тарифов
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.tariffs_list_button,
                           do_assert=True, wait="lst")

    tariff_list = TariffsList(base.driver)
    # Клик по кнопке добавления нового тарифа
    tariff_list.click_button(tariff_list.add_tariff_button)

    add_tariff = FTLTariffAdd(base.driver)
    # Выбор типа тарифа "FTL"
    add_tariff.dropdown_without_input(add_tariff.tariff_type_select, "FTL")
    # Выбор подтипа тарифа "Почасовой"
    add_tariff.dropdown_without_input(add_tariff.ftl_type_select, "Почасовой")
    # Ввод названия тарифа
    add_tariff.input_in_field(add_tariff.tariff_name_input, f"ПЧ-{base.get_timestamp()}")
    # Выбор типа ТС "до 0.5т"
    add_tariff.dropdown_without_input(add_tariff.vehicle_type_select, "до 0.5т")
    # Установка флага "Закрытый кузов"
    add_tariff.click_button(add_tariff.body_type_closed_checkbox)
    # Ввод минимальной стоимости
    add_tariff.click_button(add_tariff.price_input)
    add_tariff.input_in_field(add_tariff.hourly_params_input, base.random_value_float_str(3000, 5000))
    # Подтверждение и сохранение тарифа
    add_tariff.click_button(add_tariff.add_hourly_tariff_button, do_assert=True)
    add_tariff.click_button(add_tariff.confirm_button, wait="lst")
    # Конец теста


@allure.story("Critical path test")
@allure.feature('Создание тарифов')
@allure.description('ЛКЗ. Тест создания FTL тарифа: тип - Фиксированный, маршрут - Екб-Уфа, название - ГГ-timestamp, '
                    'ТС - 1.5т/9м3/4п, кузов - Закрытый, минималка/доп.адрес/ожидание - Рандом')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_ftl_cc_tariff_add_lkz(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к списку тарифов
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.tariffs_list_button,
                           do_assert=True, wait="lst")

    tariff_list = TariffsList(base.driver)
    # Клик по кнопке добавления нового тарифа
    tariff_list.click_button(tariff_list.add_tariff_button)

    add_tariff = FTLTariffAdd(base.driver)
    # Выбор типа тарифа "FTL"
    add_tariff.dropdown_without_input(add_tariff.tariff_type_select, "FTL")
    # Выбор подтипа тарифа "Фиксированный"
    add_tariff.dropdown_without_input(add_tariff.ftl_type_select, "Фиксированный")
    # Ввод названия тарифа
    add_tariff.input_in_field(add_tariff.tariff_name_input, f"ГГ-{base.get_timestamp()}")
    # Выбор типа маршрута "Нас. пункт - Нас. пункт"
    add_tariff.dropdown_without_input(add_tariff.fixed_type_select, "Нас. пункт - Нас. пункт")
    # Ввод города отправления
    add_tariff.dropdown_with_input(add_tariff.departures_city_input, wait_presence=True,
                                   option_text="г Екатеринбург")
    # Ввод города прибытия
    add_tariff.dropdown_with_input(add_tariff.arrival_city_input, wait_presence=True,
                                   option_text="г Уфа")
    # Выбор типа ТС "1.5т / 9м3 / 4пал."
    add_tariff.dropdown_without_input(add_tariff.vehicle_type_select, "1.5т / 9м3 / 4пал.")
    # Установка флага "Закрытый кузов"
    add_tariff.click_button(add_tariff.body_type_closed_checkbox)
    # Ввод минимальной стоимости
    add_tariff.click_button(add_tariff.price_input)
    add_tariff.input_in_field(add_tariff.fixed_params_input, base.random_value_float_str(5000, 10000))
    # Ввод стоимости доп. адреса
    add_tariff.click_button(add_tariff.address_cost_input)
    add_tariff.input_in_field(add_tariff.fixed_params_input, base.random_value_float_str(1000, 3000))
    # Ввод времени ожидания
    add_tariff.click_button(add_tariff.free_downtime_input)
    add_tariff.input_in_field(add_tariff.fixed_params_input, base.random_value_float_str(10, 60))
    # Подтверждение и сохранение тарифа
    add_tariff.click_button(add_tariff.add_fm_tariff_button, do_assert=True)
    add_tariff.click_button(add_tariff.confirm_button, wait="lst")
    # Конец теста


@allure.story("Critical path test")
@allure.feature('Создание тарифов')
@allure.description('ЛКЗ. Тест создания FTL тарифа: тип - Фиксированный, маршрут - Точка-Точка, '
                    'название - ТТ-timestamp, ТС - 1.5т/9м3/4п, адреса - Первый и Второй в списке, '
                    'кузов - Закрытый, минималка/доп.адрес/ожидание - Рандом')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_ftl_pp_tariff_add_lkz(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к списку тарифов
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.tariffs_list_button,
                           do_assert=True, wait="lst")

    tariff_list = TariffsList(base.driver)
    # Клик по кнопке добавления нового тарифа
    tariff_list.click_button(tariff_list.add_tariff_button)

    add_tariff = FTLTariffAdd(base.driver)
    # Выбор типа тарифа "FTL"
    add_tariff.dropdown_without_input(add_tariff.tariff_type_select, "FTL")
    # Выбор подтипа тарифа "Фиксированный"
    add_tariff.dropdown_without_input(add_tariff.ftl_type_select, "Фиксированный")
    # Ввод названия тарифа
    add_tariff.input_in_field(add_tariff.tariff_name_input, f"ТТ-{base.get_timestamp()}")
    # Выбор первого адреса
    add_tariff.click_button(add_tariff.first_address_select, wait="lst")
    add_tariff.click_button(add_tariff.select_first_radio)
    add_tariff.click_button(add_tariff.confirm_address_button)
    time.sleep(3)
    # Выбор второго адреса
    add_tariff.click_button(add_tariff.second_address_select, wait="lst")
    add_tariff.click_button(add_tariff.select_second_radio)
    add_tariff.click_button(add_tariff.confirm_address_button)
    # Выбор типа ТС "3т / 16м3 / 6пал."
    add_tariff.dropdown_without_input(add_tariff.vehicle_type_select, "3т / 16м3 / 6пал.")
    # Установка флага "Закрытый кузов"
    add_tariff.click_button(add_tariff.body_type_closed_checkbox)
    # Ввод минимальной стоимости
    add_tariff.click_button(add_tariff.price_input)
    add_tariff.input_in_field(add_tariff.fixed_params_input, base.random_value_float_str(5000, 10000))
    # Ввод стоимости доп. адреса
    add_tariff.click_button(add_tariff.address_cost_input)
    add_tariff.input_in_field(add_tariff.fixed_params_input, base.random_value_float_str(1000, 3000))
    # Ввод времени ожидания
    add_tariff.click_button(add_tariff.free_downtime_input)
    add_tariff.input_in_field(add_tariff.fixed_params_input, base.random_value_float_str(10, 60))
    # Подтверждение и сохранение тарифа
    add_tariff.click_button(add_tariff.add_fm_tariff_button, do_assert=True)
    add_tariff.click_button(add_tariff.confirm_button, wait="lst")
    # Конец теста


@allure.story("Critical path test")
@allure.feature('Создание тарифов')
@allure.description('ЛКЗ. Тест создания FTL тарифа: тип - Пробег, маршрут - Екб-Члб, название - ПБ-timestamp, '
                    'ТС - 5т/36м3/15п, кузов - Закрытый, минималка/доп.адрес/ожидание - Рандом')
@pytest.mark.parametrize('base_fixture', ['lkz'], indirect=True)  # Параметризация роли
def test_ftl_ml_tariff_add_lkz(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к списку тарифов
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.tariffs_list_button,
                           do_assert=True, wait="lst")

    tariff_list = TariffsList(base.driver)
    # Клик по кнопке добавления нового тарифа
    tariff_list.click_button(tariff_list.add_tariff_button)

    add_tariff = FTLTariffAdd(base.driver)
    # Выбор типа тарифа "FTL"
    add_tariff.dropdown_without_input(add_tariff.tariff_type_select, "FTL")
    # Выбор подтипа тарифа "Пробег"
    add_tariff.dropdown_without_input(add_tariff.ftl_type_select, "Пробег")
    # Ввод названия тарифа
    add_tariff.input_in_field(add_tariff.tariff_name_input, f"ПБ-{base.get_timestamp()}")
    # Выбор типа ТС "5т / 36м3 / 15пал."
    add_tariff.dropdown_without_input(add_tariff.vehicle_type_select, "5т / 36м3 / 15пал.")
    # Установка флага "Закрытый кузов"
    add_tariff.click_button(add_tariff.body_type_closed_checkbox)
    # Ввод стоимости пробега
    add_tariff.click_button(add_tariff.extra_mileage_input)
    add_tariff.input_in_field(add_tariff.mileage_params_input, base.random_value_float_str(10, 50))
    # Ввод стоимости доп. адреса
    add_tariff.click_button(add_tariff.address_cost_input)
    add_tariff.input_in_field(add_tariff.mileage_params_input, base.random_value_float_str(1000, 3000))
    # Ввод времени ожидания
    add_tariff.click_button(add_tariff.free_downtime_input)
    add_tariff.input_in_field(add_tariff.mileage_params_input, base.random_value_float_str(10, 60))
    # Ввод минимальной стоимости
    add_tariff.click_button(add_tariff.add_min_price_button)
    add_tariff.input_in_field(add_tariff.mileage_params_input, base.random_value_float_str(2500, 10000))
    # Подтверждение изменений тарифа
    add_tariff.click_button(add_tariff.add_confirm_button)
    add_tariff.input_in_field(add_tariff.mileage_params_input, base.random_value_float_str(10, 30))
    add_tariff.input_in_field(add_tariff.mileage_params_input_2, base.random_value_float_str(1, 5))
    add_tariff.input_in_field(add_tariff.mileage_params_input_3, base.random_value_float_str(10, 60))
    # Сохранение изменений тарифа
    add_tariff.click_button(add_tariff.add_fm_tariff_button, do_assert=True)
    add_tariff.click_button(add_tariff.confirm_button, wait="lst")
    # Конец теста
