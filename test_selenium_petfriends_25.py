import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('C:/Users/Алена/Downloads/chromedriver_win32/chromedriver.exe')
    # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends1.herokuapp.com/login')

    yield

    pytest.driver.quit()


def test_show_my_pets():
    # Вводим email
    pytest.driver.find_element_by_id('email').send_keys('alndn@mail.ru')
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys('112233')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    # Проверяем, что мы оказались на странице "все питомцы"
    assert WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located([By.CSS_SELECTOR, "html > body > div > div > div:nth-of-type(2)"]))
    # Нажимаем на кнопку "мои питомцы"
    pytest.driver.find_element_by_class_name('navbar-toggler-icon').click()
    # Проверяем, что мы оказались на странице "мои питомцы"
    pytest.driver.find_element_by_xpath('//*[contains(text(),"Мои питомцы")]').click()
    pytest.driver.implicitly_wait(10)
   # Количество питомцев в блоке статистики пользователя
   pets_statistic = pytest.driver.find_elements_by_xpath('//div[@class=".col-sm-4 left"]')
   # Определяем список с количеством карточек питомцев
   descriptions = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]//tbody/tr')
   # Получаем количество питомцев с фотографией
   images = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]//img')
   # Получаем список питомцев с именами
   names = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]//td[1]')
   name_true = []
   for i in names:
       name_true.append(i.text)

   assert statistics == len(descriptions) # смотрим питомцев

   for i in range(len(names)):
       assert images[i].get_attribute('src') != '' # смотрим наличие фотографий у всех питомцев
       assert statistics == len(images) # смотрим, что хотя бы у половины питомцев есть фото
       assert names[i].text != '' # смотрим, что у всех питомцев есть имя
       assert descriptions[i].text != '' # смотрим, что все карточки заполнены
       assert statistics == len(names) # смотрим, что все питомцы имеют имя возраст и породу

# Смотрим, что нет повторяющихся питомцев
   assert len(Counter(all_pets)) == len(all_pets)
   # Смотрим, что имя каждого животного уникально
   assert len(Counter(list_names)) == len(list_names)
   # Смотрим, что количество строк таблицы соответствует количеству питомцев в блоке статистики пользователя
   assert f"Питомцев: {len(names)}" in amount[0].text
   # Смотрим, что минимум у половины питомцев присутствует фотография
   assert pets_with_photo >= len(names) / 2
