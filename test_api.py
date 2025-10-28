# Софья Зотина, 36-я когорта - Дипломный проект. Инженер по тестированию плюс
import requests
import json

# Базовый URL API
BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1"

def test_create_and_get_order():
    print("🚀 Запуск теста создания и получения заказа...")
    
    # Шаг 1: Создание заказа
    order_data = {
        "firstName": "Софья",
        "lastName": "Зотина",
        "address": "Москва, ул. Ленина, 1",
        "metroStation": 5,
        "phone": "+79991234567",
        "rentTime": 3,
        "deliveryDate": "2025-11-01",
        "comment": "Тестовый заказ",
        "color": ["BLACK"]
    }
    
    try:
        # Запрос на создание заказа
        print("📦 Создаем заказ...")
        create_response = requests.post(f"{BASE_URL}/orders", json=order_data)
        
        # Проверяем успешное создание
        assert create_response.status_code == 201, f"Ошибка создания заказа: {create_response.status_code}"
        print("✅ Заказ создан успешно!")
        
        # Шаг 2: Сохраняем номер трека
        response_data = create_response.json()
        track_number = response_data["track"]
        assert track_number is not None, "Трек номер не получен"
        print(f"📮 Трек номер: {track_number}")
        
        # Шаг 3: Получение заказа по треку
        print("🔍 Получаем данные заказа по треку...")
        get_response = requests.get(f"{BASE_URL}/orders/track", params={"t": track_number})
        
        # Шаг 4: Проверяем код ответа
        assert get_response.status_code == 200, f"Ошибка получения заказа: {get_response.status_code}"
        print("✅ Данные заказа получены успешно!")
        
        # Дополнительная проверка
        order_info = get_response.json()
        assert "order" in order_info, "Ключ 'order' отсутствует в ответе"
        
        print("🎉 Все тесты пройдены успешно!")
        
    except Exception as e:
        print(f"❌ Ошибка при выполнении теста: {e}")
        raise

if __name__ == "__main__":
    test_create_and_get_order()
