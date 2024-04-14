import allure
from tests.base_test import base_test_with_login
from pages.profile_page import Profile


@allure.feature('Редактирование профиля')
@allure.description('ЛКП. Тест редактирования профиля: адреса - А-timestamp, тлф - Рандом, '
                    'налогообложение - Перебор всех вариантов без сохранения, документообор - Вкл./Выкл, '
                    'ссылка контура - Копирование, счет - 405+Рандом, бик - Фикс.')
def test_profile_edit_lkp(domain):
    base, sidebar = base_test_with_login(domain=domain, role='lkp')

    sidebar.click_button(sidebar.profile_button, do_assert=True, wait="form")

    profile = Profile(base.driver)
    profile.backspace_and_input(profile.fact_address_input, f"ФА-{base.get_timestamp()}")
    profile.backspace_and_input(profile.post_address_input, f"ПА-{base.get_timestamp()}")
    profile.backspace_and_input(profile.phone_input, base.random_value_int_str(9000000000, 9999999999))
    profile.dropdown_click_input_click(profile.vat_type_select, "Не плательщик НДС")
    profile.dropdown_click_input_click(profile.vat_type_select, "Плательщик НДС")
    profile.dropdown_click_input_click(profile.direct_request_select, "Только плательщикам НДС")
    profile.dropdown_click_input_click(profile.direct_request_select, "Только неплательщикам НДС")
    profile.dropdown_click_input_click(profile.direct_request_select, "Всем")
    profile.dropdown_click_input_click(profile.values_in_system_select, "Без НДС")
    profile.dropdown_click_input_click(profile.values_in_system_select, "С НДС")
    profile.click_button(profile.electronic_document_toggl)
    profile.click_button(profile.electronic_document_toggl)
    profile.click_button(profile.save_button, do_assert=True)
    profile.click_button(profile.confirm_button)
    profile.click_button(profile.contour_link, do_assert=True)

    base.driver.execute_script("window.scrollTo(0, 0);")

    profile.click_button(profile.additional_info_tab, do_assert=True)
    profile.backspace_and_input(profile.checking_account_input,
                                base.random_value_int_str(40500000000000000000, 40599999999999999999))
    profile.backspace_and_input(profile.bik_input, base.random_value_custom_start('046577904', 9))
    profile.click_button(profile.save_button, do_assert=True)
    profile.click_button(profile.confirm_button, wait="lst")

    sidebar.finish_test()
