# Flask-Redis-Docker

Реализован веб-сервис для обработки данных.
Контекст задачи:
  от пользователя получаются данные каждый день, таким образом каждая точка данных соответствует некоторой дате все данные имеют тип float
  в результате сбора данных мы имеем массивы вида [{"date": ..., "value": ...}, {"date": ..., "value": ...}, ...]
  видов (например шаги, средняя частота пульса и тп) данных может быть много, они однозначно различаются по строковому названию (см. примеры запросов к АПИ ниже)
  как данные попадают к нам и как они технически храняться - за рамками данной задачи

ТЗ выглядит следующим образом:

    Реализовать HTTP веб-сервис. Сервис должен предоставлять HTTP API с помощью которого можно посчитать корреляцию по Пирсону между 2 векторами данных разных типов
    При расчете корреляции требуется сопоставить потоки между собой с учетом дат, то есть мы "сравниваем" два показателя за одну и ту же дату, а не как попало
    Полученные результаты должны сохраняться в базу данных.
    Данные сохраненные в БД также должны быть впоследствии доступны в через API.

API

    POST /calculate

    Принимает входные данные в JSON-формате:

    {
        "user_id": int,
        "data": {
            "x_data_type": str,
            "y_data_type": str,
            "x": [
                {
                    "date": YYYY-MM-DD,
                    "value": float,
                },
                ...
            ],
            "y": [
                {
                    "date": YYYY-MM-DD,
                    "value": float,
                },
                ...
            ]
        }
    }

    GET /correlation?x_data_type=str&y_data_type=str&user_id=int
        Отдает посчитанную метрику для конкретного пользователя и конкретных типов данных
        Если для данной комбинации рассчитанных данных нет - возвращает 404

    Формат ответа в случае HTTP 200:

   {
       "user_id": int,
       "x_data_type": str,
       "y_data_type": str,
       "correlation": {
           "value": float,
           "p_value": float,
       }
   }

    язык Python 3.9, flask
    данные хранятся персистентно в рамках сервиса (БД Redis)
    сборка через docker compose: отдельно БД, отдельно сервис
   
   Запуск приложения:
   
   Установка:

    1. Склонируйте репозиторий
    2. выполнить комманду из папки прилоения: docker-compose up
    3. выполните запросы к приложению:
      а) для добавления данных в БД: curl -d '{"user_id":"1","data":{"x_data_type":"test_x","y_data_type":"test_y","x":[{"date":"2022-01-01","value":"100"},{"date":"2022-01-02","value":"200"}],"y": [{"date":"2022-01-01","value":"110"}, {"date":"2022-01-02","value":"220"}]}}' -H "Content-Type: application/json" -X POST http://localhost:5000/post/calculate
      
       б) для получения результатов вычисления: curl -X GET "http://0.0.0.0:5000/get/correlation?x_data_type=test_x&y_data_type=test_y&user_id=1"

   
