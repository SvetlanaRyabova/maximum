class MainPageOnlineLocators:
    BUTTON_AUTH_LOGIN = '//button[@id="login"]'
    INPUT_LOGIN = '//input[@data-test-id="login_formfield_input"]'
    INPUT_PASSWORD = '//input[@data-test-id="password_field_input"]'
    BUTTON_SUBMIT_AUTH = '//button[@data-test-id="submit-credentials-button_button"]'
    BUTTON_BANNER_CERTIFICATE = '//button[@data-test-id="banner-close_buttonicon"]'
    TEXT_PASSWORD_MUST_BE_VALID = '//p[contains(text(), "Количество символов в пароле должно быть 6 или более")]'
    TEXT_ENTRY_IS_NOT_POSSIBLE = '//p[contains(text(), "Вход недоступен")]'
    TEXT_FILL_THE_FIELD = '//p[contains(text(), "Заполните поле")]'
    BUTTON_BECOME_CLIENT = '//button[@data-test-id="auth-as-guest"]'
    TEXT_GIVE_PHONE_NUMBER = '//h2[contains(text(), "Укажите телефон")]'




