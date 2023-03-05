# Registration_login: регистрация аккаунта
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
# time.sleep(5)
# # Закрытие вкладки "Add blocker"
# driver.switch_to.window(driver.window_handles[1])
# driver.close()
# driver.switch_to.window(first_browser_tab)
# time.sleep(2)
# # Нажатие на вкладку "My Account"
# find_my_acc_btn = driver.find_element('link text', 'My Account')
# find_my_acc_btn.click()
# time.sleep(2)
# # Ввод email для регистрации
# find_reg_email_field = driver.find_element('id', 'reg_email')
# find_reg_email_field.send_keys('fortestbysergey@gmail.com')
# time.sleep(2)
# # Ввод пароля для регистрации
# find_reg_pass_field = driver.find_element('id', 'reg_password')
# find_reg_pass_field.send_keys('fortestbysergey@gmail.comABC!@#17')
# time.sleep(2)
# # Нажатие на кнопку "Register"
# find_reg_btn = driver.find_element('css selector', 'p.woocomerce-FormRow.form-row>input.woocommerce-Button.button')
# find_reg_btn.click()
# time.sleep(2)
# driver.close()

# # Registration_login: логин в систему
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
# time.sleep(5)
# # Закрытие вкладки "Add blocker"
# driver.switch_to.window(driver.window_handles[1])
# driver.close()
# driver.switch_to.window(first_browser_tab)
# time.sleep(2)
# # Нажатие на вкладку "My Account"
# find_my_acc_btn = driver.find_element('link text', 'My Account')
# find_my_acc_btn.click()
# time.sleep(2)
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
# # Проверка, что на странице есть элемент "Logout"
# check_logout_element = driver.find_element('css selector', 'li.woocommerce-MyAccount-navigation-link.woocommerce-MyAccount-navigation-link--customer-logout')
# check_logout_element_text = check_logout_element.text
# assert check_logout_element_text == 'Logout'
# if check_logout_element_text == 'Logout':
#     print('Проверка пройдена!')
# else:
#     print('Проверка НЕ пройдена!')
# time.sleep(2)
# driver.close()
