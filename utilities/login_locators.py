from selenium.webdriver.common.by import By


class LoginLocatorFields:
    email_address_field = (By.ID, "input-email")
    password_field = (By.ID, "input-password")
    login_button = (By.XPATH, "//div[@id='content']//input[@value='Login']")
    warning_message = (By.CSS_SELECTOR, "#account-login .alert-danger")
