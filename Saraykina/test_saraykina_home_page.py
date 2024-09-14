from playwright.sync_api import Page,expect
from allure import id,step,suite,story,tag,title,epic,description,label


@tag('Chromeum Autotest')
@epic('Saraykina'' Page')
@story('Matrix переход по соцсетям')
class TestMatrix:
    @id('2')
    @title('Переход по иконкам')
    @label('priority', 'Низкий')
    @description('Проверка перехода по иконкам соцсетей')
    @suite('Соцсети')
    def test_matrix_goto_to_vk(self, page: Page):
        with step('Войти на страницу Таронумерология с Алиной Сарайкиной'):
            page.goto('https://www.saraykina-numerolog.ru/index.html')

        with step('Проверить переход на страницу в VK через иконку VK'):
            with step('Перейти по иконке VK на страницу соцсети VK'):
                page.locator('//a[@href="https://vk.com/id225051986"]').click()
            with step('Проверить отображение текста ВК'):
                page.locator('#owner_page_name').is_visible()

    @id('3')
    @title('Переход по иконкам')
    @label('priority', 'Низкий')
    @description('Проверка перехода по иконкам соцсетей Telegram')
    @suite('Соцсети')
    def test_matrix_goto_to_telegram(self, page: Page):
        with step('Войти на страницу Таронумерология с Алиной Сарайкиной'):
            page.goto('https://www.saraykina-numerolog.ru/index.html')

        with step('Проверить переход на страницу в Telegram через иконку Telegram'):
            with step('Перейти по иконке Telegram на страницу соцсети Telegram'):
                page.locator('//a[@href="https://t.me/+nnZWj2D-qC84YmZi"]').click()
            with step('Проверить отображение текста Telegram'):
                page.locator('#tgme_action_button_label').is_visible()




















