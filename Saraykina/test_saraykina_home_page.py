from playwright.sync_api import Page,expect
from allure import id,step,suite,story,tag,title,epic,description,label


@tag('Chromeum Autotest')
@epic('Wiki Page')
@story('Matrix переход по соцсетям')
class TestMatrix:
    @id('2')
    @title('Поиск информации по полю "Поиск"')
    @label('priority', 'Низкий')
    @description('Проверка перехода по иконкам соцсетей')
    @suite('Соцсети')
    def test_matrix_goto_to_vk(self,page:Page):
        with step('Войти на страницу Таронумерология с Алиной Сарайкиной'):
            page.goto('https://www.saraykina-numerolog.ru/index.html')
        with step('Проверить переход на страницу в VK через иконку VK'):
            with step('Перейти по иконке VK на страницу соцсети VK'):
                pass















