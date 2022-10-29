# Bookings
analysis of hotel booking data


Импортируйте библиотеку pandas как pd. Загрузите датасет bookings.csv с разделителем ;. Проверьте размер таблицы, типы переменных, а затем выведите первые 7 строк, чтобы посмотреть на данные. 
Приведите названия колонок к нижнему регистру и замените пробелы на знак нижнего подчеркивания.
Пользователи из каких стран совершили наибольшее число успешных бронирований? Укажите топ-5.
На сколько ночей в среднем бронируют отели разных типов?
Иногда тип номера, полученного клиентом (assigned_room_type), отличается от изначально забронированного (reserved_room_type). Такое может произойти, например, по причине овербукинга. Сколько подобных наблюдений встретилось в датасете?
Проанализируйте даты запланированного прибытия. 
– На какой месяц чаще всего успешно оформляли бронь в 2016? Изменился ли самый популярный месяц в 2017?
– Сгруппируйте данные по годам и проверьте, на какой месяц бронирования отеля типа City Hotel отменялись чаще всего в каждый из периодов.
Посмотрите на числовые характеристики трёх переменных: adults, children и babies. Какая из них имеет наибольшее среднее значение?
Создайте колонку total_kids, объединив children и babies. Отели какого типа в среднем пользуются большей популярностью у клиентов с детьми?
Создайте переменную has_kids, которая принимает значение True, если клиент при бронировании указал хотя бы одного ребенка (total_kids), и False – в противном случае. Посчитайте отношение количества ушедших пользователей к общему количеству клиентов, выраженное в процентах (churn rate). Укажите, среди какой группы показатель выше.
 

Описание данных
Имеются следующие переменные:

Hotel – тип отеля (City Hotel или Resort Hotel)  
Is canceled – бронирование было отменено (1) или нет (0); неотменённое считается успешным
Lead time – количество дней, прошедших между датой бронирования и датой прибытия  
Arrival full date – полная дата прибытия
Arrival date year – год прибытия  
Arrival date month – месяц прибытия  
Arrival date week number – номер недели прибытия
Arrival date day of month – день прибытия
Stays in weekend nights – количество выходных (суббота или воскресенье), которые гость забронировал для проживания в отеле
Stays in week nights – количество дней (с понедельника по пятницу), которые гость забронировал для проживания в отеле
Stays total nights – общее число забронированных ночей (сумма двух предыдущих колонок)
Adults – число взрослых
Children – число детей
Babies – число младенцев 
Meal – выбранный тип питания
Country – страна происхождения клиента
Reserved room type – тип зарезервированного номера
Assigned room type – тип полученного номера (может отличаться от забронированного)
Customer type – тип бронирования
Reservation status – значение последнего статуса брони: Canceled – было отменено клиентом; Check-Out – клиент зарегистрировался, но уже покинул отель; No-Show – клиент не зарегистрировался и сообщил администрации отеля причину
Reservation status date – дата обновления статуса
