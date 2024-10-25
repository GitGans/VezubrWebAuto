import allure
import requests


def test_api_login_lkp(api_base_url, api_login):
    # Логинимся под ролью "lkp"
    token = api_login("lkp")
    
    # Эндпоинт для тестирования
    url = f"{api_base_url}/employee/front-settings"
    
    # Выводим эндпоинт в консоль
    print(f"Request URL: {url}")
    
    # Логируем эндпоинт в Allure
    with allure.step(f"Sending request to URL: {url}"):
        headers = {
            "Authorization": token  # Отправляем токен без 'Bearer'
        }
        
        # Отправляем запрос
        response = requests.get(url, headers=headers)
        
        # Дополнительный вывод для отладки
        print(f"Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")
        
        # Логируем результат в Allure
        with allure.step(f"Response status: {response.status_code}, Response text: {response.text}"):
            pass
    
    # Проверка статуса
    assert response.status_code == 200, "Failed to access secure endpoint"
    