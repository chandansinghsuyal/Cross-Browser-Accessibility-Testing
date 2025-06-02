import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from src.utils.browser_manager import get_driver  # Uncomment when browser_manager.py is implemented

def get_driver(browser_name='chrome'):
    if browser_name == 'chrome':
        return webdriver.Chrome()
    elif browser_name == 'firefox':
        return webdriver.Firefox()
    elif browser_name == 'edge':
        return webdriver.Edge()
    else:
        raise ValueError(f'Unsupported browser: {browser_name}')

URLS = [
    'https://www.wikipedia.org',
    'https://www.python.org',
]

@pytest.mark.parametrize('url', URLS)
def test_images_have_alt_text(url):
    driver = get_driver('chrome')
    driver.get(url)
    images = driver.find_elements(By.TAG_NAME, 'img')
    for img in images:
        alt = img.get_attribute('alt')
        assert alt is not None and alt.strip() != '', f'Image missing alt text: {img.get_attribute("src")}'
    driver.quit()

@pytest.mark.parametrize('url', URLS)
def test_aria_labels(url):
    driver = get_driver('chrome')
    driver.get(url)
    elements = driver.find_elements(By.XPATH, '//*[@aria-label]')
    for el in elements:
        aria = el.get_attribute('aria-label')
        assert aria is not None and aria.strip() != '', f'Element missing ARIA label: {el.tag_name}'
    driver.quit()

@pytest.mark.parametrize('url', URLS)
def test_keyboard_navigation(url):
    driver = get_driver('chrome')
    driver.get(url)
    body = driver.find_element(By.TAG_NAME, 'body')
    body.send_keys(Keys.TAB)
    # Check if focus is visible after tabbing
    focused = driver.switch_to.active_element
    assert focused is not None, 'No element focused after TAB'
    driver.quit() 