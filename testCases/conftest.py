

import pytest
from selenium import webdriver


@pytest.fixture()

def setup():
    d = webdriver.Chrome()
    d.get("https://admin-demo.nopcommerce.com/")
    d.maximize_window()
    return d