import pytest
import pytest_selenium
from selenium import webdriver
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("https://petfriends1.herokuapp.com/my_pets")
photo = driver.find_element_by_id("img")  #не понятно как тут писать id, если его нет
# это локатор на все фото ('//*[@id="all_my_pets"]//img')
name = driver.find_element_by_id("name") #то же самое ('//*[@id="all_my_pets"]//td[1]')
age = driver.find_element_by_id("age")  #то же самое ('//*[@id="all_my_pets"]//td[3]')
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver.get("https://petfriends1.herokuapp.com/my_pets")
element = WebDriverWait(driver, 10).until(
EC.presence_of_element_located((By.ID, "all_my_pets"))
)

@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Firefox(r'Users\Tanchik_13\geckodriver.exe')
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends1.herokuapp.com/login')

   yield

   pytest.driver.quit()

def test_show_my_pets():
   # Вводим email
   pytest.driver.find_element_by_id('email').send_keys('dsfdsf@mail.ru')
   # Вводим пароль
   pytest.driver.find_element_by_id('pass').send_keys('12345')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"
   # Переходим на страницу со своими питомцами
   pytest.driver.find_element_by_xpath("//*[@id='navbarNav']/ul[1]/li[1]/a[1]").click()
   # Проверяем, что мы оказались на странице с таблицей своих питомцев
   assert pytest.driver.find_element_by_tag_name('h2').text == "dsf"
   # кол-во питомцев = количество строк в таблице - 1 (шапка)
   ammount_of_pets = pytest.driver.find_elements_by_tag_name('tr')
   ammount_of_pets_with_photo = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
   # ??можно по-другому искать кол-во фото и потом взять часть:
   # ammount_of_pets_with_photo = pytest.driver.find_elements_by_ xpath('//*[@id="all_my_pets"]//img')
   names = pytest.driver.find_elements_by_css_selector('.card-deck .card-title')
   descriptions = pytest.driver.find_elements_by_css_selector('.card-deck .card-text')

   for i in range(len(names)):
      assert ammount_of_pets[i].count == 4
      assert ammount_of_pets_with_photo[i].count >= 2
      assert names[i].text != ''
      assert descriptions[i].text != ''
      parts = descriptions[i].text.split(", ")
      assert len(parts[0]) > 0
      assert len(parts[1]) > 0
      assert list_names(names)  # создаем список из имен
      assert set(list_names)  # превращаем список в множество, где не будет дублирующих элементов


