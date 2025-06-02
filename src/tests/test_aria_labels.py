import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver

@pytest.mark.parametrize('url', ['https://www.wikipedia.org'])
def test_aria_roles(url):
    driver = webdriver.Chrome()
    driver.get(url)
    elements = driver.find_elements(By.XPATH, '//*[@role]')
    for el in elements:
        role = el.get_attribute('role')
        assert role is not None and role.strip() != '', f'Element missing ARIA role: {el.tag_name}'
    driver.quit() 