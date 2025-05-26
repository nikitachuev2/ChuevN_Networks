# Практическая работа № 4

**Выполнил:** Чуев Никита Сергеевич  
**Группа:** P4150  
**Преподаватель:** Васильев Дмитрий Евгеньевич  
**Дата выполнения задания:** 26.05.2025  
**Название дисциплины:** "Сети и протоколы"  

## Задание

Вам нужно найти самостоятельно сайт (с открытым API) либо поднять его самостоятельно (например, решение, которое я сегодня использовал как пример на лекции https://github.com/meowle)

далее, вам нужно поработать с методами HTTP (создать, обновить, удалить)

все логи нужно перекинуть в гит либо в MD файлик с разбиением на части 

найденные сайты прикладывать в чат, у каждого будет свой сайтик (либо можете поднять мявл, почему бы и нет)

# 🍽️ API Логи — Ресторанное меню

##  Базовый URL

http://localhost:3000/dishes

##  POST — Добавление блюда

curl -X POST http://localhost:3000/dishes ^
-H "Content-Type: application/json" ^
-d "{\"name\":\"Пельмени\",\"price\":290,\"category\":\"Горячее\"}"

**Ответ:**

Microsoft Windows [Version 10.0.26100.4061]
(c) Корпорация Майкрософт (Microsoft Corporation). Все права защищены.

C:\Users\NikitaShuyiv\Desktop\ITNO\2_семестр\сети и протоколы\ChuevN_Networks\Practic№4>curl -X POST http://localhost:3000/dishes ^
Продолжить? -H "Content-Type: application/json" ^
Продолжить? -d "{\"name\":\"Пельмени\",\"price\":290,\"category\":\"Горячее\"}"
{
  "id": "381b",
  "name": "Пельмени",
  "price": 290,
  "category": "Горячее"
}
C:\Users\NikitaShuyiv\Desktop\ITNO\2_семестр\сети и протоколы\ChuevN_Networks\Practic№4>

## PUT — Обновление блюда


curl -X PUT http://localhost:3000/dishes/2 ^
-H "Content-Type: application/json" ^
-d "{\"id\":2,\"name\":\"Цезарь с креветками\",\"price\":350,\"category\":\"Салаты\"}"


**Ответ:**


Microsoft Windows [Version 10.0.26100.4061]
(c) Корпорация Майкрософт (Microsoft Corporation). Все права защищены.

C:\Users\NikitaShuyiv\Desktop\ITNO\2_семестр\сети и протоколы\ChuevN_Networks\Practic№4>curl -X PUT http://localhost:3000/dishes/2 ^
Продолжить? -H "Content-Type: application/json" ^
Продолжить? -d "{\"id\":2,\"name\":\"Цезарь с креветками\",\"price\":350,\"category\":\"Салаты\"}"
{
  "id": "2",
  "name": "Цезарь с креветками",
  "price": 350,
  "category": "Салаты"
}
C:\Users\NikitaShuyiv\Desktop\ITNO\2_семестр\сети и протоколы\ChuevN_Networks\Practic№4>

##  DELETE — Удаление блюда


curl -X DELETE http://localhost:3000/dishes/1


**Ответ:**

Microsoft Windows [Version 10.0.26100.4061]
(c) Корпорация Майкрософт (Microsoft Corporation). Все права защищены.

C:\Users\NikitaShuyiv\Desktop\ITNO\2_семестр\сети и протоколы\ChuevN_Networks\Practic№4>curl -X DELETE http://localhost:3000/dishes/1
{
  "id": "1",
  "name": "Борщ",
  "price": 250,
  "category": "Супы",
  "description": "Традиционный русский борщ с говядиной, свеклой, капустой и сметаной",
  "vegetarian": false
}
C:\Users\NikitaShuyiv\Desktop\ITNO\2_семестр\сети и протоколы\ChuevN_Networks\Practic№4>