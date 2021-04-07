from allure_commons.types import Severity
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
import allure


@allure.title('Test Result is More Than 10')
@allure.severity(Severity.BLOCKER)
def test_yandex_search():
    driver = WebDriver(executable_path='/usr/local/bin/chromedriver')
    # driver.set_page_load_timeout(30)
    with allure.step('Opening Search window'):
        driver.get("https://ya.ru")
    # driver.maximize_window()

    with allure.step('Looking for market.yandex.ru'):
        # Using the X-path to search an element in this case.
        search_input = driver.find_element_by_xpath('//input[@id="text"]')
        # Using nested X-path inside one element (the search2__button in this case).
        search_button = driver.find_element_by_xpath('//div[@class="search2__button"]//button[@type="submit"]')
        # Entering the input into the search panel.
        search_input.send_keys('market.yandex.ru')
        search_button.click()

    def check_result_count(driver):
        inner_search_results = driver.find_elements_by_xpath('//li[@class="serp-item"]')
        return len(inner_search_results) >= 10
    with allure.step('Expecting that result will be >= 10'):

        # The check_result_count is sending as a link to function in this case - not function itself.
        WebDriverWait(driver, 5, 0.5).until(check_result_count, 'Number of elements is less then 10')

    with allure.step('Go through the First link'):
        search_results = driver.find_elements_by_xpath('//li[@class="serp-item"]')
        # Looking in the inner collection of the element (the h2 in this case).
        link = search_results[0].find_element_by_xpath('.//h2/a')
        link.click()

    driver.switch_to.window(driver.window_handles[1])
    with allure.step('Checking of correct Title of the page'):
        assert driver.title == 'Яндекс.Маркет — выбор и покупка товаров из проверенных интернет-магазинов'

    # We don`t close the window of the browser to se the end of result.
