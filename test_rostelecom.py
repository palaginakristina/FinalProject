from pages.auth_page import AuthPage
from pages.reg_page import RegPage
from pages.locators import *
from settings import *
import pytest


@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.add_argument("--start-maximized")
    return chrome_options

#Тестирование страницы Авторизация

#ТС1
#@pytest.mark.skip()
def test_start_page_is_correct_phone(selenium):
    ''' Тестирование ТЗ: Проверка табов выбора в форме Авторизация '''
    page = AuthPage(selenium)
    assert page.phone.is_enabled(), "Авторизация: поле для ввода телефона/почты/логина/лиц счета неактивно"


#TC2
#@pytest.mark.skip()
def test_start_page_is_correct_password(selenium):
    ''' Тестирование ТЗ: Проверка поля для ввода пароля в форме Авторизация '''
    page = AuthPage(selenium)
    assert page.password.is_enabled(), "Авторизация: поле для ввода пароля неактивно"


#ТС3
#@pytest.mark.skip()
#@pytest.mark.xfail(reason="Таб выбора должен называться 'Номер'")
def test_start_page_is_correct_tab_phone(selenium):
    ''' Тестирование ТЗ: Проверка наименования таба Номер в форме Авторизация '''
    page = AuthPage(selenium)
    assert page.tab_phone.text == "Номер", "Таб выбора Номер не соответствует ТЗ"


#ТС4
#@pytest.mark.skip()
def test_start_page_is_correct_tab_mail(selenium):
    ''' Тестирование ТЗ: Проверка наименования таба Почта в форме Авторизация '''
    page = AuthPage(selenium)
    assert page.tab_mail.text == "Почта", "Таб выбора Почта не соответствует ТЗ"


#ТС5
#@pytest.mark.skip()
def test_start_page_is_correct_tab_login(selenium):
    ''' Тестирование ТЗ: Проверка наименования таба Логин в форме Авторизация '''
    page = AuthPage(selenium)
    assert page.tab_login.text == "Логин", "Таб выбора Логин не соответствует ТЗ"


#ТС6
#@pytest.mark.skip()
def test_start_page_is_correct_tab_ls(selenium):
    ''' Тестирование ТЗ: Проверка наименования таба Лицевой счет в форме Авторизация '''
    page = AuthPage(selenium)
    assert page.tab_ls.text == "Лицевой счёт", "Таб выбора Лицевой счет не соответствует ТЗ"


#ТС7
#@pytest.mark.skip()
def test_user_with_invalid_password(selenium):
    '''Тестирование отображения ошибки при валидном лицевом счете и невалидном пароле'''

    page = AuthPage(selenium)
    page.tab_ls.click() # активировали таб Лицевой счет
    result = page.enter_login_or_password(selenium, pers_account, password_invalid) # ввод лиц. счета и пароля
    assert result == 'Неверный логин или пароль', "Не отобразилась ошибка при неверном лицевом счете или пароле"

#ТС8
#@pytest.mark.skip()
def test_link_color_forgot_password(selenium):
    '''Тестирование: при вводе неправильного пароля элемент 'Забыли пароль' перекрашивается в оранжевый цвет'''

    page = AuthPage(selenium)
    page.tab_ls.click() # активировали таб Лицевой счет
    page.enter_login_or_password(selenium, pers_account, password_invalid) # ввод лицевого счета и пароля
    assert "rt-link--orange" in page.forget_password_link.get_attribute('class'), "В соответствии с ТЗ цвет ссылки должен был измениться "


#Тестирование страницы Регистрация

#ТС9
#@pytest.mark.skip()
def test_registration(selenium):
    ''' форма Авторизация: проверка перехода по ссылке "Зарегистрироваться" '''
    page = AuthPage(selenium)
    page.reg_link.click()
    assert page.find_el(*AuthLocators.reg_page_reg_text).text == 'Регистрация'


#ТС10
#@pytest.mark.skip()
def test_reg_page_name_field_text(selenium):
    ''' Тестирование ТЗ: Проверка наименования поля Имя в форме Регистрация '''
    page = RegPage(selenium)
    assert page.name_field_text.text == 'Имя', "Наименование поля Имя не соответствует ТЗ"


#ТС11
#@pytest.mark.skip()
def test_reg_page_last_name_field_text(selenium):
    ''' Тестирование ТЗ: Проверка наименования в поле Фамилия в форме Регистрация '''
    page = RegPage(selenium)
    assert page.last_name_field_text.text == 'Фамилия', "Наименование поля Фамилия не соответствует ТЗ"


#ТС12
#@pytest.mark.skip()
def test_reg_page_region_field_text(selenium):
    ''' Тестирование ТЗ: Проверка надписи в поле Регион в форме Регистрация '''
    page = RegPage(selenium)
    assert page.region_field_text.text == 'Регион', "Наименование поля Регион не соответствует ТЗ"


#ТС13
#@pytest.mark.skip()
def test_reg_page_email_or_mobile_phone_field_text(selenium):
    ''' Тестирование ТЗ: Проверка надписи в поле "E-mail или мобильный телефон" в форме Регистрация '''
    page = RegPage(selenium)
    assert page.email_or_mobile_phone_field_text.text == 'E-mail или мобильный телефон', \
        "Наименование поля Емайл или моб.тел. не соответствует ТЗ"


#ТС14
#@pytest.mark.skip()
def test_reg_page_password_field_text(selenium):
    ''' Тестирование ТЗ: Проверка надписи в поле Пароль в форме Регистрация '''
    page = RegPage(selenium)
    assert page.password_field_text.text == 'Пароль', "Наименование поля Пароль не соответствует ТЗ"


#ТС15
#@pytest.mark.skip()
def test_reg_page_password_confirmation_field_text(selenium):
    ''' Тестирование ТЗ: Проверка надписи в поле 'Подтверждение пароля' в форме Регистрация '''
    page = RegPage(selenium)
    assert page.password_confirmation_field_text.text == 'Подтверждение пароля', \
        "Наименование поля Подтверждение пароля не соответствует ТЗ"


#ТС16
#@pytest.mark.skip()
#@pytest.mark.xfail(reason="Кнопка должна называться 'Продолжить'")
def test_reg_page_button_continue(selenium):
    ''' Тестирование ТЗ: Проверка названия кнопки "Продолжить" в форме Регистрация '''
    page = RegPage(selenium)
    assert page.page_continue_button.text == 'Продолжить', "Наименование кнопки Продолжить не соответствует ТЗ"



#ТС17
@pytest.fixture(scope="function", params=[
 ("", "Пустое имя", "Необходимо заполнить поле кириллицей. От 2 до 30 символов."),
 (" ", "Пробел", "Необходимо заполнить поле кириллицей. От 2 до 30 символов."),
 ("-", "Тире", "Тест позитивный. Сообщения об ошибке нет"),
 ("В", "Имя из одной буквы", "Необходимо заполнить поле кириллицей. От 2 до 30 символов."),
 ("Ви", "Имя из двух букв", "Тест позитивный. Сообщения об ошибке нет"),
 ("Паа", "Имя из трёх букв", "Тест позитивный. Сообщения об ошибке нет"),
 ("ПетяОльгаВладимирАлександрЕгор", "Имя из 30 букв", "Тест позитивный. Сообщения об ошибке нет"),
 ("ИмяИмяИмяИмяИмяИмяИмяИмяИмяИмяИ", "Имя из 31 буквы", "Необходимо заполнить поле кириллицей. От 2 до 30 символов."),
 ("Дима-Василий", "Двойное имя через тире", "Тест позитивный. Сообщения об ошибке нет"),
 ("python","Имя латиницей", "Необходимо заполнить поле кириллицей. От 2 до 30 символов."),
 ("2727", "Имя цифрами", "Необходимо заполнить поле кириллицей. От 2 до 30 символов."),
 ("#$%", "Имя спецсимволами", "Необходимо заполнить поле кириллицей. От 2 до 30 символов.")
])
def param_name(request):
   return request.param

#ТС18
#@pytest.mark.skip()
def test_registration_page_name_field(selenium, param_name):
    ''' Тестирование формы Регистрация: отображение ошибки при вводе некорректного имени '''
    page = RegPage(selenium)
 (input, description, expected_output) = param_name
    result = page.reg_name_field_send(selenium, input)
    print("Имя: {0}\nОписание: {1}\nОжидаемая ошибка: {2}".format(input, description, expected_output))


    assert result == expected_output, "Реакция на имя: " + description + " - не соответствует ТЗ"


#ТС19
#@pytest.mark.skip()
#@pytest.mark.xfail(reason="Неправильное сообщение об ошибке, если без заглавной буквы и нет цифр и спецсимволов")
@pytest.mark.parametrize("input, description, expected_output",
[
 ("", "Пусто", "Длина пароля должна быть не менее 8 символов"),
 (" ", "Пробел", "Длина пароля должна быть не менее 8 символов"),
 ("Пароль русскими", "Кириллица", "Пароль должен содержать только латинские буквы"),
 ("1", "Одна цифра", "Длина пароля должна быть не менее 8 символов"),
 ("Rython pytho1", "Содержит пробел", "Пароль не должен содержать пробелов"),
 ("Python15@", "Позитивный тест", "Тест позитивный. Сообщения об ошибке нет"),
 ("pythonpython", "Латиницей без заглавной", "Пароль должен содержать хотя бы одну заглавную букву"),
],
    ids=
[
    "Empty",
    "Space",
    "Cyrillic",
    "One digit",
    "Contains a space",
    "Positive test",
    "Latin without a capital letter",
])
def test_registration_page_password_field(selenium, input, description, expected_output):
    ''' Тестирование формы Регистрация: отображение ошибки при вводе некорректного пароля '''
    page = RegPage(selenium)
    result = page.reg_password_field_send(selenium, input)
    print("Пароль: {0}\nОписание: {1}\nОжидаемая ошибка: {2}".format(input, description, expected_output))


    assert result == expected_output, "Реакция на пароль: " + description + "- не соответствует ТЗ"


# Запуск тестов:
# pytest -v -s -q --driver Chrome --driver-path C:/Users/duda-/PycharmProjects/pythonProject/FinalProject/chromedriver.exe test_rostelecom.py