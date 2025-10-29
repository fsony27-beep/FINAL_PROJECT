# Софья Зотина, 36-я когорта — Дипломный проект. Инженер по тестированию плюс

import sender_stand_request
import data.order_data

def test_create_and_get_order():
    # Создаем заказ
    order_body = data.order_data.get_order_body()
    order_response = sender_stand_request.post_new_order(order_body)
    
    # Получаем трек
    track = order_response.json()["track"]
    
    # Получаем заказ по треку
    get_response = sender_stand_request.get_order_by_track(track)
    assert get_response.status_code == 200