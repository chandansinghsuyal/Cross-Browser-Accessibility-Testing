from selenium import webdriver

def get_driver(browser_name='chrome'):
    if browser_name == 'chrome':
        return webdriver.Chrome()
    elif browser_name == 'firefox':
        return webdriver.Firefox()
    elif browser_name == 'edge':
        return webdriver.Edge()
    else:
        raise ValueError(f'Unsupported browser: {browser_name}') 