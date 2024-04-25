from base.base_class import Base
from pages.login_page import Login
from pages.sidebar import SideBar


def base_test_with_login(domain, role):
    base = Base.get_driver()

    login = Login(base.driver, domain)
    login.authorization(role)

    sidebar = SideBar(base.driver)
    sidebar.click_button(sidebar.sidebar_button)

    return base, sidebar


def base_test_without_login(domain):
    base = Base.get_driver()

    login = Login(base.driver, domain)
    login.registration_start()

    return base, login


def base_test_with_login_via_link(domain):
    base = Base.get_driver()

    login = Login(base.driver, domain)
    login.registration_via_link(domain)

    return base, login
