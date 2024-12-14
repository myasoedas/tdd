from django.test import TestCase


class HomePageTest(TestCase):
    def test_home_page_uses_correct_template(self):
        """
        Проверяем, что домашняя страница использует правильный шаблон.
        """
        response = self.client.get("/")
        self.assertTemplateUsed(response, "lists/home.html")

    def test_home_page_contains_correct_html(self):
        """
        Проверяем, что HTML содержит ожидаемый заголовок.
        """
        response = self.client.get("/")
        self.assertContains(response, "<title>To-Do lists</title>")

    def test_home_page_returns_http_200(self):
        """
        Проверяем, что сервер возвращает HTTP 200.
        """
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
