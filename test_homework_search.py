from selene.support.shared import browser
from selene import be, have


def test_search_yashaka_github(open_firefox_with_given_resolution):
    browser.open('')
    browser.element('[type="search"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="center_col"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


def test_googl_search_stub(open_firefox_with_given_resolution):
    browser.open('')
    input_text = 'iausdfhgoidsygfhisuadyfgdsakuyfgdsaukyfgdsaukfyasgduf'
    browser.element('[type="search"]').type(input_text).press_enter()
    browser.element('[class="card-section"]').should(have.text(f'По запросу {input_text} ничего не найдено.'))

