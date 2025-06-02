import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

@pytest.mark.parametrize('url', ['https://www.wikipedia.org'])
def test_tab_order(url):
    driver = webdriver.Chrome()
    driver.get(url)
    body = driver.find_element(By.TAG_NAME, 'body')
    tab_order = []
    for _ in range(10):
        body.send_keys(Keys.TAB)
        focused = driver.switch_to.active_element
        tab_order.append(focused)
    # Check for duplicates in tab order
    assert len(tab_order) == len(set(tab_order)), 'Tab order has duplicates or is not linear'
    driver.quit() 