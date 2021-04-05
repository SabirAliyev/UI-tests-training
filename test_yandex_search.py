from selenium.webdriver.firefox.webdriver import WebDriver


def test_yandex_search():
    driver = WebDriver(executable_path='/usr/local/bin/geckodriver')
    driver.set_page_load_timeout(30)
    driver.get("https://ya.ru")
    driver.maximize_window()
    print(None)
    ...