# # Shop: отображение страницы товара
# from selenium import webdriver
# import time
# from selenium.webdriver.chrome.options import Options
# path_to_extension = r'C:\Users\Shirko\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\5.4.1_0'
# chrome_options = Options()
# chrome_options.add_argument('load-extension=' + path_to_extension)
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.create_options()
# driver.maximize_window()
# first_browser_tab = driver.window_handles[0]
# driver.switch_to.window(first_browser_tab)
# # Открытие страницы
# driver.get("https://practice.automationtesting.in/")
# time.sleep(10)
# # Закрытие вкладки "Add blocker"
# driver.switch_to.window(driver.window_handles[1])
# driver.close()
# driver.switch_to.window(first_browser_tab)
# time.sleep(1)
# # Нажатие на вкладку "My Account"
# find_my_acc_btn = driver.find_element('link text', 'My Account')
# find_my_acc_btn.click()
# time.sleep(5)
# # Ввод email для входа
# find_email_field = driver.find_element('id', 'username')
# find_email_field.send_keys('fortestbysergey@gmail.com')
# time.sleep(2)
# # Ввод пароля для входа
# find_reg_pass_field = driver.find_element('id', 'password')
# find_reg_pass_field.send_keys('fortestbysergey@gmail.comABC!@#17')
# time.sleep(2)
# # Нажатие на кнопку "Login"
# find_log_btn = driver.find_element('css selector', 'p:nth-child(3)>input.woocommerce-Button.button')
# find_log_btn.click()
# time.sleep(3)
# # Нажатие на вкладку "Shop"
# find_shop_btn = driver.find_element('link text', 'Shop')
# find_shop_btn.click()
# time.sleep(3)
# # Открытие книги "HTML 5 Forms"
# find_book = driver.find_element('css selector', 'img[alt="Mastering HTML5 Forms"]')
# find_book.click()
# # Проверка, что заголовок книги назвается: "HTML5 Forms"
# check_book_name = driver.find_element('css selector', 'div.summary.entry-summary>h1')
# check_book_name_text = check_book_name.text
# assert check_book_name_text == 'HTML5 Forms'
# if check_book_name_text == 'HTML5 Forms':
#     print('Проверка пройдена!')
# else:
#     print('Проверка НЕ пройдена!')
# time.sleep(2)
# driver.close()

# # Shop: количество товаров в категории
# from selenium import webdriver
# import time
# from selenium.webdriver.chrome.options import Options
# path_to_extension = r'C:\Users\Shirko\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\5.4.1_0'
# chrome_options = Options()
# chrome_options.add_argument('load-extension=' + path_to_extension)
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.create_options()
# driver.maximize_window()
# first_browser_tab = driver.window_handles[0]
# driver.switch_to.window(first_browser_tab)
# # Открытие страницы
# driver.get("https://practice.automationtesting.in/")
# time.sleep(4)
# # Закрытие вкладки "Add blocker"
# driver.switch_to.window(driver.window_handles[1])
# driver.close()
# driver.switch_to.window(first_browser_tab)
# time.sleep(1)
# # Нажатие на вкладку "My Account"
# find_my_acc_btn = driver.find_element('link text', 'My Account')
# find_my_acc_btn.click()
# time.sleep(5)
# # Ввод email для входа
# find_email_field = driver.find_element('id', 'username')
# find_email_field.send_keys('fortestbysergey@gmail.com')
# time.sleep(2)
# # Ввод пароля для входа
# find_reg_pass_field = driver.find_element('id', 'password')
# find_reg_pass_field.send_keys('fortestbysergey@gmail.comABC!@#17')
# time.sleep(2)
# # Нажатие на кнопку "Login"
# find_log_btn = driver.find_element('css selector', 'p:nth-child(3)>input.woocommerce-Button.button')
# find_log_btn.click()
# time.sleep(3)
# # Нажатие на вкладку "Shop"
# find_shop_btn = driver.find_element('link text', 'Shop')
# find_shop_btn.click()
# time.sleep(3)
# # Открытие категории "HTML"
# find_html_part = driver.find_element('link text', 'HTML')
# find_html_part.click()
# time.sleep(5)
# # Тест отображения трех товаров
# find_lots_in_html = driver.find_elements('css selector', '.woocommerce-LoopProduct-link')
# assert len(find_lots_in_html) == 3
# if len(find_lots_in_html) == 3:
#     print('Количество товаров в разделе равно:', len(find_lots_in_html))
# else:
#     print('Количество товаров в корзине НЕ равно: '+str(len(find_lots_in_html))+'!')
# time.sleep(3)
# driver.quit()

# Shop: сортировка товаров
# from selenium import webdriver
# import time
# from selenium.webdriver.chrome.options import Options
# path_to_extension = r'C:\Users\Shirko\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\5.4.1_0'
# chrome_options = Options()
# chrome_options.add_argument('load-extension=' + path_to_extension)
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.create_options()
# driver.maximize_window()
# first_browser_tab = driver.window_handles[0]
# driver.switch_to.window(first_browser_tab)
# from selenium.webdriver.support.select import Select
# driver.implicitly_wait(25)
# # Открытие страницы
# driver.get("https://practice.automationtesting.in/")
# time.sleep(7)
# # Закрытие вкладки "Add blocker"
# driver.switch_to.window(driver.window_handles[1])
# driver.close()
# driver.switch_to.window(first_browser_tab)
# time.sleep(1)
# # Нажатие на вкладку "My Account"
# find_my_acc_btn = driver.find_element('link text', 'My Account')
# find_my_acc_btn.click()
# time.sleep(5)
# # Ввод email для входа
# find_email_field = driver.find_element('id', 'username')
# find_email_field.send_keys('fortestbysergey@gmail.com')
# time.sleep(2)
# # Ввод пароля для входа
# find_reg_pass_field = driver.find_element('id', 'password')
# find_reg_pass_field.send_keys('fortestbysergey@gmail.comABC!@#17')
# time.sleep(2)
# # Нажатие на кнопку "Login"
# find_log_btn = driver.find_element('css selector', 'p:nth-child(3)>input.woocommerce-Button.button')
# find_log_btn.click()
# time.sleep(3)
# # Нажатие на вкладку "Shop"
# find_shop_btn = driver.find_element('link text', 'Shop')
# find_shop_btn.click()
# time.sleep(3)
# # Тест, что в селекторе выбран вариант сортировки по умолчанию
# search_status_selector = driver.find_element('name', 'orderby')
# status_checked = search_status_selector.get_attribute("value")
# assert status_checked == 'menu_order'
# time.sleep(2)
# if status_checked == 'menu_order':
#     print('Статус: Default sorting')
# else:
#     print('Статус: НЕ Default sorting')
# time.sleep(3)
# # Сортировка товаров по цене от большей к меньшей
# find_selector = driver.find_element('name', 'orderby')
# select = Select(find_selector)
# select.select_by_index("5")
# time.sleep(3)
# # Тест, что выбрана сортировка товаров по цене от большей к меньшей
# search_status_selector2 = driver.find_element('name', 'orderby')
# status2_checked = search_status_selector2.get_attribute("value")
# assert status2_checked == 'price-desc'
# time.sleep(2)
# if status2_checked == 'price-desc':
#     print('Статус: Sort by price: high to low')
# else:
#     print('Статус: НЕ Sort by price: high to low')
# time.sleep(3)
# driver.quit()

# Shop: отображение, скидка товара
# from selenium import webdriver
# import time
# from selenium.webdriver.chrome.options import Options
# path_to_extension = r'C:\Users\Shirko\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\5.4.1_0'
# chrome_options = Options()
# chrome_options.add_argument('load-extension=' + path_to_extension)
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.create_options()
# driver.maximize_window()
# first_browser_tab = driver.window_handles[0]
# driver.switch_to.window(first_browser_tab)
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# driver.implicitly_wait(25)
# # Открытие страницы
# driver.get("https://practice.automationtesting.in/")
# time.sleep(7)
# # Закрытие вкладки "Add blocker"
# driver.switch_to.window(driver.window_handles[1])
# driver.close()
# driver.switch_to.window(first_browser_tab)
# time.sleep(1)
# # Нажатие на вкладку "My Account"
# find_my_acc_btn = driver.find_element('link text', 'My Account')
# find_my_acc_btn.click()
# time.sleep(5)
# # Ввод email для входа
# find_email_field = driver.find_element('id', 'username')
# find_email_field.send_keys('fortestbysergey@gmail.com')
# time.sleep(2)
# # Ввод пароля для входа
# find_reg_pass_field = driver.find_element('id', 'password')
# find_reg_pass_field.send_keys('fortestbysergey@gmail.comABC!@#17')
# time.sleep(2)
# # Нажатие на кнопку "Login"
# find_log_btn = driver.find_element('css selector', 'p:nth-child(3)>input.woocommerce-Button.button')
# find_log_btn.click()
# time.sleep(3)
# # Нажатие на вкладку "Shop"
# find_shop_btn = driver.find_element('link text', 'Shop')
# find_shop_btn.click()
# time.sleep(3)
# # Открытие книги "Android Quick Start Guide"
# find_android_book = driver.find_element('css selector', '[alt="Android Quick Start Guide"]')
# find_android_book.click()
# time.sleep(3)
# # Тест, что содержимое старой цены = "₹600.00"
# find_old_prise = driver.find_element('css selector', 'del>span')
# find_old_prise_text = find_old_prise.text
# assert find_old_prise_text == '₹600.00'
# if find_old_prise_text == '₹600.00':
#     print('Старая цена:', find_old_prise_text)
# else:
#     print('Старая цена НЕ равна', find_old_prise_text)
# # Тест, что содержимое новой цены = "₹450.00"
# find_new_prise = driver.find_element('css selector', 'ins>span')
# find_new_prise_text = find_new_prise.text
# assert find_new_prise_text == '₹450.00'
# if find_new_prise_text == '₹450.00':
#     print('Новая цена:', find_new_prise_text)
# else:
#     print('Новая цена НЕ равна', find_new_prise_text)
# time.sleep(3)
# # Явное ожидание и нажатие на обложку книги.
# search_book_img = WebDriverWait(driver, 15).until(
#      EC.element_to_be_clickable((By.CSS_SELECTOR, '[alt="Android Quick Start Guide"]')))
# search_book_img.click()
# time.sleep(2)
# # Явное ожидание и закрытие обложки.
# search_close_img = WebDriverWait(driver, 15).until(
#      EC.element_to_be_clickable((By.CSS_SELECTOR, ' div.pp_details>a')))
# search_close_img.click()
# time.sleep(3)
# driver.quit()

# Shop: проверка цены в корзине
# from selenium import webdriver
# import time
# from selenium.webdriver.chrome.options import Options
# path_to_extension = r'C:\Users\Shirko\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\5.4.1_0'
# chrome_options = Options()
# chrome_options.add_argument('load-extension=' + path_to_extension)
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.create_options()
# driver.maximize_window()
# first_browser_tab = driver.window_handles[0]
# driver.switch_to.window(first_browser_tab)
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# driver.implicitly_wait(25)
# # Открытие страницы
# driver.get("https://practice.automationtesting.in/")
# time.sleep(7)
# # Закрытие вкладки "Add blocker"
# driver.switch_to.window(driver.window_handles[1])
# driver.close()
# driver.switch_to.window(first_browser_tab)
# time.sleep(1)
# # Нажатие на вкладку "My Account"
# find_my_acc_btn = driver.find_element('link text', 'My Account')
# find_my_acc_btn.click()
# time.sleep(5)
# # Ввод email для входа
# find_email_field = driver.find_element('id', 'username')
# find_email_field.send_keys('fortestbysergey@gmail.com')
# time.sleep(2)
# # Ввод пароля для входа
# find_reg_pass_field = driver.find_element('id', 'password')
# find_reg_pass_field.send_keys('fortestbysergey@gmail.comABC!@#17')
# time.sleep(2)
# # Нажатие на кнопку "Login"
# find_log_btn = driver.find_element('css selector', 'p:nth-child(3)>input.woocommerce-Button.button')
# find_log_btn.click()
# time.sleep(3)
# # Нажатие на вкладку "Shop"
# find_shop_btn = driver.find_element('link text', 'Shop')
# find_shop_btn.click()
# time.sleep(3)
# # Добавление в корзину книги "Mastering JavaScript"
# find_book = driver.find_element('css selector', '[alt="Mastering JavaScript"]')
# find_book.click()
# time.sleep(1)
# find_add_to_basket_btn = driver.find_element('css selector', '.single_add_to_cart_button.button.alt')
# find_add_to_basket_btn.click()
# time.sleep(1)
# # Тест, что возле корзины количество товаров = "1 Item", а стоимость = "₹350.00"
# find_num_of_item = driver.find_element('css selector', 'span.cartcontents')
# find_num_of_item_text = find_num_of_item.text
# assert find_num_of_item_text == '1 Item'
# if find_num_of_item_text == '1 Item':
#     print('Количество товаров в корзине:', find_num_of_item_text)
# else:
#     print('Количество товаров в корзине НЕ равно', find_num_of_item_text)
# time.sleep(2)
# find_prise = driver.find_element('css selector', 'a>span.amount')
# find_prise_text = find_prise.text
# assert find_prise_text == '₹350.00'
# if find_prise_text == '₹350.00':
#     print('Стоимость товара в корзине:', find_prise_text)
# else:
#     print('Стоимость товара в корзине НЕ равно', find_prise_text)
# time.sleep(2)
# # Явное ожидание и проверка, что в Subtotal отобразилась стоимость.
# find_basket = driver.find_element('css selector', '.wpmenucart-contents')
# find_basket.click()
# search_subportal_text = WebDriverWait(driver, 15).until(
#      EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'tr.cart-subtotal>td>span'), find_prise_text))
# assert search_subportal_text is True
# time.sleep(3)
# # Явное ожидание и проверка, что в Total отобразилась стоимость.
# search_total_text = WebDriverWait(driver, 15).until(
#      EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'td>strong>span'), '₹357.00'))
# assert search_total_text is True
# time.sleep(3)
# driver.quit()

# Shop: работа в корзине
# from selenium import webdriver
# import time
# from selenium.webdriver.chrome.options import Options
# path_to_extension = r'C:\Users\Shirko\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\5.4.1_0'
# chrome_options = Options()
# chrome_options.add_argument('load-extension=' + path_to_extension)
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.create_options()
# driver.maximize_window()
# first_browser_tab = driver.window_handles[0]
# driver.switch_to.window(first_browser_tab)
# driver.implicitly_wait(25)
# # Открытие страницы
# driver.get("https://practice.automationtesting.in/")
# time.sleep(7)
# # Закрытие вкладки "Add blocker"
# driver.switch_to.window(driver.window_handles[1])
# driver.close()
# driver.switch_to.window(first_browser_tab)
# time.sleep(1)
# # Нажатие на вкладку "My Account"
# find_my_acc_btn = driver.find_element('link text', 'My Account')
# find_my_acc_btn.click()
# time.sleep(5)
# # Ввод email для входа
# find_email_field = driver.find_element('id', 'username')
# find_email_field.send_keys('fortestbysergey@gmail.com')
# time.sleep(2)
# # Ввод пароля для входа
# find_reg_pass_field = driver.find_element('id', 'password')
# find_reg_pass_field.send_keys('fortestbysergey@gmail.comABC!@#17')
# time.sleep(2)
# # Нажатие на кнопку "Login"
# find_log_btn = driver.find_element('css selector', 'p:nth-child(3)>input.woocommerce-Button.button')
# find_log_btn.click()
# time.sleep(3)
# # Нажатие на вкладку "Shop"
# find_shop_btn = driver.find_element('link text', 'Shop')
# find_shop_btn.click()
# time.sleep(3)
# # Скролл вниз на 300 пикселей
# driver.execute_script("window.scrollBy(0, 300);")
# time.sleep(2)
# # Добавление в корзину книги "Mastering JavaScript" (остальные "Out of stock")
# find_add_to_basket_btn = driver.find_element('css selector', 'a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart')
# find_add_to_basket_btn.click()
# time.sleep(2)
# # Переход в корзину
# find_basket_btn = driver.find_element('css selector', '.wpmenucartli>a')
# find_basket_btn.click()
# time.sleep(2)
# # Удаление книги
# find_remove_btn = driver.find_element('css selector', 'td.product-remove>a')
# find_remove_btn.click()
# time.sleep(2)
# # Отмена удаления книги
# find_undo_btn = driver.find_element('link text', 'Undo?')
# find_undo_btn.click()
# time.sleep(2)
# # Увеличение товара в Quantity до 3 штук
# find_quantity_field = driver.find_element('css selector', 'td.product-quantity>div>input')
# find_quantity_field.clear()
# find_quantity_field.send_keys('3')
# time.sleep(3)
# # Нажатие на кнопку "UPDATE BASKET"
# find_update_btn = driver.find_element('name', 'update_cart')
# find_update_btn.click()
# # Тест, что value элемента quantity для "Mastering JavaScript" равно 3
# search_quantity_value = driver.find_element('name', 'cart[9766527f2b5d3e95d4a733fcfb77bd7e][qty]')
# status_checked = search_quantity_value.get_attribute("value")
# assert status_checked == '3'
# if status_checked == '3':
#     print('Value для Quantity равно:', status_checked)
# else:
#     print('Value для Quantity НЕ равно', status_checked)
# time.sleep(2)
# # Нажатие на кнопку "APPLY COUPON"
# find_apply_coupon_btn = driver.find_element('name', 'apply_coupon')
# time.sleep(2)
# find_apply_coupon_btn.click()
# # Тест, что возникло сообщение: "Please enter a coupon code."
# find_text = driver.find_element('css selector', 'div.woocommerce>ul>li')
# find_text_text = find_text.text
# assert find_text_text == 'Please enter a coupon code.'
# time.sleep(1)
# driver.quit()

# Shop: покупка товара
# from selenium import webdriver
# import time
# from selenium.webdriver.chrome.options import Options
# path_to_extension = r'C:\Users\Shirko\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\5.4.1_0'
# chrome_options = Options()
# chrome_options.add_argument('load-extension=' + path_to_extension)
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.create_options()
# driver.maximize_window()
# first_browser_tab = driver.window_handles[0]
# driver.switch_to.window(first_browser_tab)
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.keys import Keys
# driver.implicitly_wait(25)
# # Открытие страницы
# driver.get("https://practice.automationtesting.in/")
# time.sleep(7)
# # Закрытие вкладки "Add blocker"
# driver.switch_to.window(driver.window_handles[1])
# driver.close()
# driver.switch_to.window(first_browser_tab)
# time.sleep(1)
# # Нажатие на вкладку "My Account"
# find_my_acc_btn = driver.find_element('link text', 'My Account')
# find_my_acc_btn.click()
# time.sleep(5)
# # Ввод email для входа
# find_email_field = driver.find_element('id', 'username')
# find_email_field.send_keys('fortestbysergey@gmail.com')
# time.sleep(2)
# # Ввод пароля для входа
# find_reg_pass_field = driver.find_element('id', 'password')
# find_reg_pass_field.send_keys('fortestbysergey@gmail.comABC!@#17')
# time.sleep(2)
# # Нажатие на кнопку "Login"
# find_log_btn = driver.find_element('css selector', 'p:nth-child(3)>input.woocommerce-Button.button')
# find_log_btn.click()
# time.sleep(3)
# # Нажатие на вкладку "Shop"
# find_shop_btn = driver.find_element('link text', 'Shop')
# find_shop_btn.click()
# time.sleep(3)
# # Скролл вниз на 300 пикселей
# driver.execute_script("window.scrollBy(0, 300);")
# time.sleep(2)
# # Добавление в корзину книги "Mastering JavaScript" (остальные "Out of stock")
# find_add_to_basket_btn = driver.find_element('css selector', 'a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart')
# find_add_to_basket_btn.click()
# time.sleep(2)
# # Переход в корзину
# find_basket_btn = driver.find_element('css selector', '.wpmenucartli>a')
# find_basket_btn.click()
# time.sleep(2)
# # Явное ожидание и нажатие кнопки "Proceed to Checkout".
# find_proceed_to_checkout_btn = WebDriverWait(driver, 15).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, '.checkout-button.button.alt.wc-forward')))
# find_proceed_to_checkout_btn.click()
# time.sleep(5)
# # Заполнение обязательных полей
# find_first_name_field = WebDriverWait(driver, 15).until(
#     EC.element_to_be_clickable((By.ID, 'billing_first_name')))
# find_first_name_field.clear()
# find_first_name_field.send_keys('Sergey')
# find_last_name_field = driver.find_element('id', 'billing_last_name')
# find_last_name_field.clear()
# find_last_name_field.send_keys('Shirko')
# find_email_field = driver.find_element('id', 'billing_email_field')
# find_last_name_field.clear()
# find_last_name_field.send_keys('fortestbysergey@gmail.com')
# find_phone_field = driver.find_element('id', 'billing_phone')
# find_phone_field.clear()
# find_phone_field.send_keys('123456789')
# find_country_selector = driver.find_element('id', 's2id_billing_country')
# find_country_selector.click()
# find_country_selector_field = driver.find_element('id', 's2id_autogen1_search')
# find_country_selector_field.send_keys('New Zealand')
# find_country_selector_field.send_keys(Keys.ENTER)
# find_street_field = driver.find_element('id', 'billing_address_1')
# find_street_field.clear()
# find_street_field.send_keys('Victory street')
# find_apartment_field = driver.find_element('id', 'billing_address_2')
# find_apartment_field.send_keys('121/2')
# find_town_field = driver.find_element('id', 'billing_city')
# find_town_field.clear()
# find_town_field.send_keys('Wellington')
# find_postcode_field = driver.find_element('id', 'billing_postcode')
# find_postcode_field.clear()
# find_postcode_field.send_keys('12345')
# # Выбор способа оплаты "Check Payments"
# driver.execute_script("window.scrollBy(0, 600);")
# time.sleep(2)
# find_radio_btn = driver.find_element('id', 'payment_method_cheque')
# find_radio_btn.click()
# # Нажатие PLACE ORDER
# find_btn_place_order = driver.find_element('id', 'place_order')
# find_btn_place_order.click()
# # Явное ожидание и проверка что отображается надпись "Thank you. Your order has been received."
# find_thanks_txt = WebDriverWait(driver, 20).until(
#  EC.text_to_be_present_in_element(('css selector', 'p.woocommerce-thankyou-order-received'), 'Thank you. Your order has been received.'))
# assert find_thanks_txt is True
# # Явное ожидание и проверка что в Payment Method отображается текст "Check Payments"
# find_payment_txt = WebDriverWait(driver, 20).until(
#  EC.text_to_be_present_in_element(('css selector', 'tr:nth-child(3)>td'), 'Check Payments'))
# assert find_payment_txt is True
# driver.quit()




