from playwright.sync_api import Page, sync_playwright
from config import SERVICE_URL


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(SERVICE_URL)
    page.wait_for_load_state('load')


def swap_text(page: Page, xpath: str, new_text: str):
    page.evaluate('''
        ({xpath, newText}) => {
            const element = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
            if (element) {
                element.innerText = newText;
            }
        }
    ''', {'xpath': xpath, 'newText': new_text})


xpath_co2 = '//*[@id="app"]/div/div[5]/div/div/div/div/div[3]/div/div[2]/div[2]'
xpath_co2_num = '//*[@id="app"]/div/div[5]/div/div/div/div/div[3]/div/div[2]/div[2]/div/div[1]'
xpath_co2_text = '//*[@id="app"]/div/div[5]/div/div/div/div/div[3]/div/div[2]/div[2]/div/div[2]'

xpath_water = '//*[@id="app"]/div/div[5]/div/div/div/div/div[3]/div/div[2]/div[4]'
xpath_water_num = '//*[@id="app"]/div/div[5]/div/div/div/div/div[3]/div/div[2]/div[4]/div/div[1]'
xpath_water_text = '//*[@id="app"]/div/div[5]/div/div/div/div/div[3]/div/div[2]/div[4]/div/div[2]'

xpath_energy = '//*[@id="app"]/div/div[5]/div/div/div/div/div[3]/div/div[2]/div[6]'
xpath_energy_num = '//*[@id="app"]/div/div[5]/div/div/div/div/div[3]/div/div[2]/div[6]/div/div[1]'
xpath_energy_text = '//*[@id="app"]/div/div[5]/div/div/div/div/div[3]/div/div[2]/div[6]/div/div[2]'


def screenshot(page: Page, selector: str, test_number: int):
    screenshot_path = f'/test_avito/output/{test_number}.png'
    page.locator(selector).screenshot(path=screenshot_path)


def test_1(page: Page):
    new_num = "999"
    page.goto(SERVICE_URL)
    swap_text(page, xpath_co2_num, new_num)
    screenshot(page, xpath_co2,1)


def test_2(page: Page):
    new_num = r"1"
    new_text = r"т CO₂"
    page.goto(SERVICE_URL)
    swap_text(page, xpath_co2_num, new_num)
    swap_text(page, xpath_co2_text, new_text)
    screenshot(page, xpath_co2,2)


def test_3(page: Page):
    new_num = r"1.001"
    new_text = r"т CO₂"
    page.goto(SERVICE_URL)
    swap_text(page, xpath_co2_num, new_num)
    swap_text(page, xpath_co2_text, new_text)
    screenshot(page, xpath_co2,3)


def test_4(page: Page):
    new_num = r"0"
    new_text = r"кг CO₂"
    page.goto(SERVICE_URL)
    swap_text(page, xpath_co2_num, new_num)
    swap_text(page, xpath_co2_text, new_text)
    screenshot(page, xpath_co2,4)


def test_5(page: Page):
    new_num = r"0"
    new_text = r"кг CO₂"
    page.goto(SERVICE_URL)
    swap_text(page, xpath_co2_num, new_num)
    swap_text(page, xpath_co2_text, new_text)
    screenshot(page, xpath_co2,5)


def test_6(page: Page):
    new_num = r"999"
    new_text = r"л воды"
    page.goto(SERVICE_URL)
    swap_text(page, xpath_water_num, new_num)
    swap_text(page, xpath_water_text, new_text)
    screenshot(page, xpath_water,6)


def test_7(page: Page):
    new_num = r"1"
    new_text = r"м³ воды"
    page.goto(SERVICE_URL)
    swap_text(page, xpath_water_num, new_num)
    swap_text(page, xpath_water_text, new_text)
    screenshot(page, xpath_water,7)


def test_8(page: Page):
    new_num = r"1.001"
    new_text = r"м³ воды"
    page.goto(SERVICE_URL)
    swap_text(page, xpath_water_num, new_num)
    swap_text(page, xpath_water_text, new_text)
    screenshot(page, xpath_water,8)


def test_9(page: Page):
    new_num = r"0"
    new_text = r"л воды"
    page.goto(SERVICE_URL)
    swap_text(page, xpath_water_num, new_num)
    swap_text(page, xpath_water_text, new_text)
    screenshot(page, xpath_water,9)


def test_10(page: Page):
    new_num = r"0"
    new_text = r"л воды"
    page.goto(SERVICE_URL)
    swap_text(page, xpath_water_num, new_num)
    swap_text(page, xpath_water_text, new_text)
    screenshot(page, xpath_water,10)


def test_11(page: Page):
    new_num = r"999"
    new_text = r"кВт⋅ч энергии"
    page.goto(SERVICE_URL)
    swap_text(page, xpath_energy_num, new_num)
    swap_text(page, xpath_energy_text, new_text)
    screenshot(page, xpath_energy,11)


def test_12(page: Page):
    new_num = "1"
    new_text = r"МВт⋅ч энергии"
    page.goto(SERVICE_URL)
    swap_text(page, xpath_energy_num, new_num)
    swap_text(page, xpath_energy_text, new_text)
    screenshot(page, xpath_energy,12)


def test_13(page: Page):
    new_num = r"1.001"
    new_text = r"МВт⋅ч энергии"
    page.goto(SERVICE_URL)
    swap_text(page, xpath_energy_num, new_num)
    swap_text(page, xpath_energy_text, new_text)
    screenshot(page, xpath_energy,13)


def test_14(page: Page):
    new_num = r"0"
    new_text = r"кВт⋅ч энергии"
    page.goto(SERVICE_URL)
    swap_text(page, xpath_energy_num, new_num)
    swap_text(page, xpath_energy_text, new_text)
    screenshot(page, xpath_energy,14)


def test_15(page: Page):
    new_num = r"0"
    new_text = r"кВт⋅ч энергии"
    page.goto(SERVICE_URL)
    swap_text(page, xpath_energy_num, new_num)
    swap_text(page, xpath_energy_text, new_text)
    screenshot(page, xpath_energy,15)


