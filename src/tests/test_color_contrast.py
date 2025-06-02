import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def luminance(rgb):
    r, g, b = [x/255.0 for x in rgb]
    a = [v/12.92 if v <= 0.03928 else ((v+0.055)/1.055)**2.4 for v in (r, g, b)]
    return 0.2126*a[0] + 0.7152*a[1] + 0.0722*a[2]

def contrast_ratio(rgb1, rgb2):
    l1 = luminance(rgb1)
    l2 = luminance(rgb2)
    return (max(l1, l2) + 0.05) / (min(l1, l2) + 0.05)

def parse_rgb(s):
    import re
    m = re.findall(r'\d+', s)
    return tuple(map(int, m[:3])) if len(m) >= 3 else (0,0,0)

@pytest.mark.parametrize('url', ['https://www.wikipedia.org'])
def test_color_contrast(url):
    driver = webdriver.Chrome()
    driver.get(url)
    elements = driver.find_elements(By.XPATH, '//*')
    for el in elements:
        fg = el.value_of_css_property('color')
        bg = el.value_of_css_property('background-color')
        fg_rgb = parse_rgb(fg)
        bg_rgb = parse_rgb(bg)
        ratio = contrast_ratio(fg_rgb, bg_rgb)
        assert ratio >= 4.5, f'Low contrast ratio: {ratio} for element {el.tag_name}'
    driver.quit() 