from selenium import webdriver

# Инициализация браузера
browser = webdriver.Firefox()

try:
    # Переход на страницу
    browser.get("http://localhost:8000")

    # Проверка заголовка страницы
    assert "To-Do" in browser.title, f"Browser title was: {browser.title}"

except AssertionError as e:
    # Если заголовок не соответствует, вывести ошибку в консоль
    print(f"Test failed: {e}")

finally:
    # Очистка: Закрытие браузера
    browser.quit()
