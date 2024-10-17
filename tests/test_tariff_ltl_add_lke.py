import allure
import pytest
from pages.tariff_ltl_add_page import LTLTariffAdd
from pages.tariffs_list_page import TariffsList


@allure.story("Smoke test")
@allure.feature('Создание тарифов')
@allure.description('ЛКЭ. Тест создания LTL тарифа: название - LTL-timestamp, тип - Короб, мин.вес/объем вес/сбор '
                    'прям./сбор обр. - Рандом, регион - Свердл/Алтай, минималка/доплата/темп.коэф/срок - Рандом')
@pytest.mark.parametrize('base_fixture', ['lke'], indirect=True)  # Параметризация роли
def test_ltl_tariff_add_lke(base_fixture, domain):
    # Инициализация базовых объектов через фикстуру
    base, sidebar = base_fixture

    # Переход к списку тарифов
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.tariffs_list_button,
                           do_assert=True, wait="lst")

    tariff_list = TariffsList(base.driver)
    # Клик по кнопке добавления нового тарифа
    tariff_list.click_button(tariff_list.add_tariff_button)

    add_tariff = LTLTariffAdd(base.driver)
    # Выбор типа тарифа "LTL"
    add_tariff.dropdown_click_input_click(add_tariff.tariff_type_select, "LTL")
    # Ввод названия тарифа
    add_tariff.input_in_field(add_tariff.tariff_name_input, f"LTL-{base.get_timestamp()}")
    # Выбор подтипа тарифа "Короб"
    add_tariff.dropdown_click_input_click(add_tariff.ltl_type_select, "Короб")
    # Ввод минимального веса
    add_tariff.backspace_len_and_input(add_tariff.min_weight_input, base.random_value_float_str(10, 100))
    # Ввод объёмного веса
    add_tariff.backspace_len_and_input(add_tariff.volumetric_weight_input, base.random_value_float_str(10, 100))
    # Ввод стоимости прямого сбора
    add_tariff.backspace_len_and_input(add_tariff.direct_price_input, base.random_value_float_str(100, 500))
    # Ввод стоимости обратного сбора
    add_tariff.backspace_len_and_input(add_tariff.reverse_price_input, base.random_value_float_str(100, 500))
    # Выбор региона отправки
    add_tariff.dropdown_with_input(add_tariff.dispatch_region_select, "Свердловская область")
    # Выбор региона доставки
    add_tariff.dropdown_with_input(add_tariff.delivery_region_select, "Алтайский край")
    # Ввод минимальной стоимости
    add_tariff.input_in_field(add_tariff.min_price_input, base.random_value_float_str(1000, 3000))
    # Ввод стоимости за килограмм
    add_tariff.input_in_field(add_tariff.kg_price_input, base.random_value_float_str(50, 200))
    # Ввод температурного коэффициента
    add_tariff.input_in_field(add_tariff.temp_coeff_input, base.random_value_float_str(1.0, 5.0))
    # Ввод срока доставки
    add_tariff.input_in_field(add_tariff.delivery_time_input, base.random_value_float_str(5, 50))
    # Подтверждение и сохранение тарифа
    add_tariff.click_button(add_tariff.add_tariff_button, do_assert=True)
    add_tariff.click_button(add_tariff.confirm_add_button, wait="lst")
    # Конец теста
