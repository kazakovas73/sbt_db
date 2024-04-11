# sbt_db
Repo for homework

# HW 3
- Создал БД и добавил запись
![Снимок экрана (5)](https://github.com/kazakovas73/sbt_db/assets/71931438/5641bc60-e0b8-4b7b-b0e8-ac960ef59cd3)

- Подключился к БД в коде
![Снимок экрана 2024-04-11 233219](https://github.com/kazakovas73/sbt_db/assets/71931438/ea735c7f-277a-4666-9421-257cafc64d7e)

- Проверил, что фамилия есть
![Снимок экрана (7)](https://github.com/kazakovas73/sbt_db/assets/71931438/0bf91868-e0c3-4bfe-b543-0d32c5d4e385)

- Остановил сервер
![Снимок экрана 2024-04-11 232935](https://github.com/kazakovas73/sbt_db/assets/71931438/9f4ce3b0-929e-40b4-8eff-0692ac8a3e8b)

- Проверил, что фамилия осталась
![Снимок экрана (8)](https://github.com/kazakovas73/sbt_db/assets/71931438/552c110f-74f9-4de7-b6d7-9bd57dfdb86f)


# HW 2
Сохранил большой JSON (>40МБ) в виде разных структур - строка, hset, zset, list и протестировал скорость сохранения и чтения
![image](https://github.com/kazakovas73/sbt_db/assets/71931438/bb01df59-ed81-4a73-acf0-430fdb2e6324)
По второй части задания: создал docker-compose файл из трех контейнеров, а также conf файл для redis, который содержит условия из задания.


# HW 1
Сначала я создал Dockerfile, который создает контейнер с образом mongo и скачал json датасет с песнями репера Дрейка. Потом создал контейнер из образа и запустил его, также запустил mongo shell, где подгрузил датасет и провел CRUD операции.

- docker build -t mongo .
<img width="518" alt="Снимок экрана 2024-03-13 191002" src="https://github.com/kazakovas73/sbt_db/assets/71931438/bda299ca-f480-4c4b-8da0-918c7920b3e5">

- docker run mongo
<img width="695" alt="Снимок экрана 2024-03-13 191016" src="https://github.com/kazakovas73/sbt_db/assets/71931438/aea778ec-f2b3-41da-97b7-33948cabba08">

- docker ps
<img width="608" alt="Снимок экрана 2024-03-13 191746" src="https://github.com/kazakovas73/sbt_db/assets/71931438/581bf9d5-0d44-4200-b5c4-4df0d57a75ea">

- docker exec -it 5158ab4ef2e9 /bin/bash
- mongoimport --jsonArray --db drake --collection drake_data --file drake_data.json
<img width="577" alt="Снимок экрана 2024-03-13 191453" src="https://github.com/kazakovas73/sbt_db/assets/71931438/72515ff6-7d83-4aef-9460-ead1d7041462">

- mongosh
<img width="700" alt="Снимок экрана 2024-03-13 191042" src="https://github.com/kazakovas73/sbt_db/assets/71931438/37790e7f-7998-4d6c-b72f-2e507c134874">

- use drake
- db.drake_data.findOne()
<img width="472" alt="Снимок экрана 2024-03-13 191913" src="https://github.com/kazakovas73/sbt_db/assets/71931438/cb30037b-88da-4e3e-b76f-6bc1a06a3e79">

- db.drake_data.insertOne({album: "New album", lyrics_title: "New song", lyrics_url: "google.com", lyrics: "ABC", track_views: "1"})
<img width="692" alt="Снимок экрана 2024-03-13 193405" src="https://github.com/kazakovas73/sbt_db/assets/71931438/cbbbf9f6-930d-4115-b6c9-36e042b0e701">

- db.drake_data.find({track_views: "1"})
<img width="261" alt="Снимок экрана 2024-03-13 193542" src="https://github.com/kazakovas73/sbt_db/assets/71931438/5121603b-c975-4f2b-b157-3793ec2a48ba">

- db.drake_data.updateOne({track_views: { $eq: "1" }}, { $set: { album: "Very new album" }})
<img width="543" alt="Снимок экрана 2024-03-13 193940" src="https://github.com/kazakovas73/sbt_db/assets/71931438/f2a3b717-83fc-403e-9ab3-1e97b09ba662">

- db.drake_data.deleteOne({track_views: "1"}) 
<img width="281" alt="Снимок экрана 2024-03-13 194100" src="https://github.com/kazakovas73/sbt_db/assets/71931438/315719fa-8a81-41fc-a2de-cfde69706487">

- db.drake_data.find({lyrics: {$regex: "my life and"}}).explain("executionStats")
- <img width="296" alt="Снимок экрана 2024-03-14 164613" src="https://github.com/kazakovas73/sbt_db/assets/71931438/1d4f58e7-7b13-4e15-8926-012f06cb9229">

- db.drake_data.createIndex({lyrics:1})
- У меня оказался слишком маленький датасет, поэтому executionTimeMillisEstimate одинаковый для операции find по конкрктному значению, а regex из прошлого пункта в 5 раз медленнее стал работать.


# HW 0
C - Consistency
A - Availability
P - Partition-tolerance

# DragonFly - CA
Dragonfly спроектирован для вертикального масштабирования на одной машине, что позволяет командам экономить затраты и усложнять управление многоузловым кластером. Для наборов данных в памяти объемом до 1 ТБ Dragonfly предлагает самое простое и надежное масштабирование на рынке.

# ArenadataDB - CP
С Arenadata DB вы построите надёжное, масштабируемое корпоративное хранилище данных, которое будет расти вместе с вашими потребностями. Arenadata DB реализована на кластере из множества (от двух до сотен) серверов и равномерно распределяет нагрузку и данные между ними. Полное соответствие принципам строгой изоляции транзакции (принципы ACID). Одни и те же таблицы могут быть использованы для записи и чтения, без страха потерять данные. Уровень изоляции транзакций — Serializable.

# ScyllaDB - AP
Любой узел может обслуживать любой запрос, нет единой точки координации, и все узлы в системе продолжают совместно предоставлять услуги, даже когда узлы становятся недоступными. Окончательная согласованность поддерживает современные рабочие нагрузки, которые в меньшей степени зависят от строгой согласованности, но в значительной степени зависят от доступности. Кластер ScyllaDB обеспечивает конечную согласованность. При окончательной согласованности все узлы реплики в конечном итоге придут к одному и тому же состоянию данных.
