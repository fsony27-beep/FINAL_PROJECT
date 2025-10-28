-- Задание 1: Курьеры с заказами в доставке
SELECT c.login, COUNT(o.id) as orders_in_delivery
FROM "Couriers" c
LEFT JOIN "Orders" o ON c.id = o."courierId"
WHERE o."inDelivery" = true
GROUP BY c.login;

-- Задание 2: Статусы заказов
SELECT track,
    CASE 
        WHEN finished = true THEN 2
        WHEN cancelled = true THEN -1
        WHEN "inDelivery" = true THEN 1
        ELSE 0
    END as status
FROM "Orders";
