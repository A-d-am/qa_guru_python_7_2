import pytest
from selene.support.shared import browser


@pytest.fixture
def open_firefox_with_given_resolution():
    browser.config.window_width = 1400
    browser.config.window_height = 1600
    browser.config.browser_name = 'firefox'
    browser.config.base_url = "https://google.com"
    yield
    browser.quit()
