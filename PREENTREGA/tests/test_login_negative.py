from utils.login_page import login

def test_login_invalid(driver):
    login(driver, user="locked_out_user", password_text="secret_sauce")

    assert "Epic sadface" in driver.page_source