import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By  # Для поиска элементов на странице


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        """
        Метод, выполняемый перед каждым тестом.
        Здесь инициализируется браузер.
        """
        self.browser = webdriver.Firefox()

    def tearDown(self):
        """
        Метод, выполняемый после каждого теста.
        Здесь закрывается браузер, чтобы не было утечек.
        """
        self.browser.quit()

    def test_can_start_a_todo_list(self):
        """
        Основной тест, проверяющий функциональность приложения.
        """
        # Эдит узнала о новом приложении для списков дел и заходит на его главную страницу
        self.browser.get("http://localhost:8000")

        # Она замечает, что заголовок страницы упоминает списки дел
        self.assertIn("To-Do", self.browser.title, f"Title was: {self.browser.title}")

        # Проверяем заголовок страницы для подтверждения корректной загрузки
        header_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn("To-Do", header_text, f"Header was: {header_text}")

        # TODO: Добавить тестовые шаги для ввода задачи и проверки результата
        self.fail("Завершите тест!")  # Оставляем как маркер для напоминания

        # Удовлетворённая, Эдит закрывает приложение

if __name__ == "__main__":
    unittest.main()
