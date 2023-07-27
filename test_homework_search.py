from selene import browser
from selene import be, have

browser.config.driver_name = 'firefox'


def test_search_yashaka_github(set_browser_resolution):
    browser.open('https://google.com')
    browser.element('[id="APjFqb"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="rcnt"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


def test_googl_search_stub():
    browser.open('https://google.com')
    input_text = 'iausdfhgoidsygfhisuadyfgdsakuyfgdsaukyfgdsaukfyasgduf'
    browser.element('[id="APjFqb"]').type(input_text).press_enter()
    browser.element('[id="rcnt"]').should(have.text(f'По запросу {input_text} ничего не найдено.'))
