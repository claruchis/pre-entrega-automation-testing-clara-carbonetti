def test_login_empty(driver):
    from utils.login_page import login

    login(driver, user="", password_text="")
    assert "Epic sadface" in driver.page_source