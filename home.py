# Home: добавление комментария
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
path_to_extension = r'C:\Users\Shirko\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\5.4.1_0'
chrome_options = Options()
chrome_options.add_argument('load-extension=' + path_to_extension)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.create_options()
driver.maximize_window()
first_browser_tab = driver.window_handles[0]
driver.switch_to.window(first_browser_tab)
# Открытие страницы
driver.get("https://practice.automationtesting.in/")
time.sleep(5)
# Закрытие вкладки "Add blocker"
driver.switch_to.window(driver.window_handles[1])
driver.close()
driver.switch_to.window(first_browser_tab)
time.sleep(2)
# Скролл страницы вниз на 600 пикселей (мне не хватило 600, поставил 900).
driver.execute_script("window.scrollBy(0, 900);")
time.sleep(2)
# Нажатие на название книги "Selenium Ruby" или на кнопку "READ MORE"
find_img_ruby = driver.find_element('css selector', 'img[title="Selenium Ruby"]')
find_img_ruby.click()
time.sleep(2)
# Нажатие на вкладку "REVIEWS"
find_reviews = driver.find_element('css selector', 'li.reviews_tab>a')
find_reviews.click()
time.sleep(2)
# Проставление 5 звёзд
find_5stars = driver.find_element('css selector', 'a.star-5')
find_5stars.click()
time.sleep(2)
# Заполнение поля "Review" сообщением: "Nice book!"
find_comment_field = driver.find_element('id', 'comment')
find_comment_field.send_keys('Nice book!')
time.sleep(2)
# Заполнение поля "Name"
find_author_field = driver.find_element('id', 'author')
find_author_field.send_keys('Sergey')
time.sleep(2)
# Заполнение "Email"
find_email_field = driver.find_element('id', 'email')
find_email_field.send_keys('email@email.ru')
time.sleep(2)
# Нажатие на кнопку "SUBMIT"
find_submit_btn = driver.find_element('css selector', '.form-submit>.submit')
find_submit_btn.click()
time.sleep(2)
driver.close()




