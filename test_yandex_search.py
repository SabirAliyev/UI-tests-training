from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


def test_yandex_search():
    driver = WebDriver(executable_path='/usr/local/bin/chromedriver')
    driver.set_page_load_timeout(30)
    driver.get("https://ya.ru")
    # driver.maximize_window()
    search_input = driver.find_element_by_xpath('//input[@id="text"]')
    search_button = driver.find_element_by_xpath('//div[@class="search2__button"]//button[@type="submit"]')
    search_input.send_keys('market.yandex.ru')
    search_button.click()

    def check_result_count(driver):
        inner_search_results = driver.find_elements_by_xpath('//li[@class="serp-item"]')
        return len(inner_search_results) >= 10

    # check_result_count is sending as link.
    WebDriverWait(driver, 5, 0.5).until(check_result_count, 'Number of elements is less then 10')

    search_results = driver.find_elements_by_xpath('//li[@class="serp-item"]')
    link = search_results[0].find_element_by_xpath('.//h2/a')
    link.click()

    driver.switch_to.window(driver.window_handles[1])

    assert driver.title == 'Яндекс.Маркет — выбор и покупка товаров из проверенных интернет-магазинов'

