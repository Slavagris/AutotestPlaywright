from playwright.sync_api import Page,expect
from allure import id,step,suite,story,tag,title,epic,description,label
class TestWiki:
    @tag('Chromeum Autotest')
    @epic('Wiki Page')
    @story('Wiki поисковик')
    class TestWiki:
        @id('1')
        @title('Поиск информации по полю "Поиск"')
        @label('priority', 'Низкий')
        def test_wiki_search_article(self, page:Page):
            with step('Войти на страницу Википедиия'):
                page.goto('https://www.wikipedia.org/')
            with step('Проверить поиск информации по полю "Поиск"'):
                with step('Написать текст в поле "Поиск"'):
                    page.fill('#searchInput', 'Гражданская война в России')
                with step('Нажать на клавиатуре кнопку "Enter"'):
                    page.press('#typeahead-suggestions', 'Enter')






