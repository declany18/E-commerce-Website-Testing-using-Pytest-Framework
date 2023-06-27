from selenium.webdriver.common.by import By


class RegistrationLocatorFields:
    registration_button = (By.PARTIAL_LINK_TEXT, "Register")
    first_name_field = (By.ID, "input-firstname")
    last_name_field = (By.ID, "input-lastname")
    registration_email_field = (By.ID, "input-email")
    phone_number_field = (By.ID, "input-telephone")
    registration_password_field = (By.ID, "input-password")
    registration_confirm_password_field = (By.ID, "input-confirm")
    privacy_checkbox = (By.XPATH, "//*[@id='content']/form/div/div/div/label")
    continue_button = (By.XPATH, "//input[@value='Continue']")
    warning_message = (By.CSS_SELECTOR, "#account-register .alert-danger")



