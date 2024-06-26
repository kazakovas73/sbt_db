# sbt_db
Repo for homework

# HW 4
# RedStore
RedStore - это мощная, высокопроизводительная база данных на основе PostgreSQL, которая разработана для работы с большими объемами данных и высокой производительностью. Она предлагает широкий спектр функций, включая распределенную архитектуру, параллельную обработку запросов, поддержку SQL, а также возможность интеграции с другими средствами аналитики и обработки данных. RedStore поддерживает распределенное хранение данных и выполнение запросов, что позволяет эффективно обрабатывать запросы и аналитику на больших объемах данных.

## История развития
База данных RedStore была создана командой профессионалов в области баз данных в компании RedCorp. Разработка началась в далеком 2010 году, когда компания столкнулась с необходимостью обработки и анализа больших объемов данных. Команда инженеров и архитекторов начала работу над новым продуктом, который мог бы эффективно хранить и обрабатывать данные, обеспечивая при этом высокую производительность и масштабируемость.

В 2012 году была выпущена первая версия RedStore, которая предложила инновационные возможности, такие как распределенное хранение данных и параллельная обработка запросов. Эти возможности сразу же привлекли внимание крупных корпораций и компаний, использующих большие объемы данных для аналитики и бизнес-процессов.

С течением времени и с улучшением технологий, база данных RedStore стала еще более мощной и универсальной. В 2015 году была выпущена версия с расширенными возможностями SQL и интеграцией с другими средствами аналитики. Команда RedCorp продолжила работу над улучшением производительности и надежности базы данных, добавляя новые функции и оптимизации.

На сегодняшний день база данных RedStore стала одним из лидеров на рынке баз данных, предлагая выдающуюся производительность, масштабируемость и надежность для компаний любого масштаба. Ее функциональность и инновации продолжают привлекать внимание новых пользователей и делают ее одной из лучших баз данных для работы с большими объемами данных.

## Инструменты для взаимодействия с СУБД
1. SQL Command Line: Интерфейс командной строки для отправки SQL запросов и управления базой данных.
2. PgAdmin: Графический инструмент для администрирования базы данных, который позволяет просматривать, редактировать и управлять объектами базы данных.
3. DBeaver: Универсальный клиент баз данных, который поддерживает множество СУБД, включая RedStore. Позволяет выполнять SQL запросы, просматривать и редактировать данные.
4. Navicat: Мощный графический инструмент для администрирования базы данных, который позволяет управлять структурой базы данных, выполнять SQL запросы и многое другое.
5. RedStore CLI: Командная строка для работы с базой данных RedStore, предоставляющая различные утилиты для управления и администрирования базы данных.

## Какой database engine используется в вашей СУБД?
В СУБД RedStore используется собственный database engine, который разработан специально для работы с этой базой данных. Этот engine оптимизирован для обработки больших объемов данных, обеспечивает высокую производительность и надежность работы базы данных. На данный момент подробности о технологиях, лежащих в основе RedStore, не разглашены, поэтому конкретные детали функционирования этого database engine остаются закрытыми.

## Как устроен язык запросов в вашей СУБД? Разверните БД с данными и выполните ряд запросов. 
Данные:
```sql
@prefix foaf:  <http://xmlns.com/foaf/0.1/> .

_:a  foaf:name   "Johnny Lee Outlaw" .
_:a  foaf:mbox   <mailto:jlow@example.com> .
_:b  foaf:name   "Peter Goodguy" .
_:b  foaf:mbox   <mailto:peter@example.org> .
_:c  foaf:mbox   <mailto:carol@example.org> .
```

```sql
PREFIX foaf:   <http://xmlns.com/foaf/0.1/>
SELECT ?name ?mbox
WHERE
  { ?x foaf:name ?name .
    ?x foaf:mbox ?mbox }
```
Результат:
name	mbox
"Johnny Lee Outlaw"	<mailto:jlow@example.com>
"Peter Goodguy"	<mailto:peter@example.org>

Данные:
```sql
@prefix foaf:  <http://xmlns.com/foaf/0.1/> .

_:a  foaf:name   "Alice" .
_:b  foaf:name   "Bob" .
```

```sql
PREFIX foaf:   <http://xmlns.com/foaf/0.1/>
SELECT ?x ?name
WHERE  { ?x foaf:name ?name }
```
Результат:
x	name
_:c	"Alice"
_:d	"Bob"


## Распределение файлов БД по разным носителям?
СУБД RedStore может использовать различные методы для распределения файлов по разным носителям для улучшения производительности и надежности. Обычно это может быть достигнуто с помощью шардирования или разделения данных на разные физические устройства.

Например, при использовании шардирования данные могут быть разделены на несколько групп, которые хранятся на разных серверах или хранилищах данных. Каждая группа данных, или шард, может содержать определенный диапазон данных или отдельный тип данных.

Другой подход - размещение различных файлов данных и журналов транзакций на разных дисках или разделах для балансировки нагрузки и повышения отказоустойчивости.

Конкретные методы и настройки распределения файлов в RedStore могут различаться в зависимости от конфигурации и требований вашей системы. Для более подробной информации рекомендуется обратиться к документации RedStore или к консультантам по базам данных.

## На каком языке/ах программирования написана СУБД?
RedStore - это облегченное хранилище удаленных рабочих столов, написанное на C с использованием библиотеки Redland.

## Какие типы индексов поддерживаются в СУБД? Приведите пример создания индексов.
RedStore поддерживает следующие типы индексов:
1. B-Tree индексы
2. GIN индексы
3. GiST индексы
4. SP-GiST индексы
5. BRIN индексы

Пример создания B-Tree индекса на таблице "users" для столбца "username":
```sql
CREATE INDEX username_idx ON users (username);
```
Пример создания GIN индекса на таблице "posts" для столбца "tags":
```sql
CREATE INDEX tags_gin_idx ON posts USING GIN (tags);
```

## Как строится процесс выполнения запросов в СУБД?
Процесс выполнения запросов в RedStore можно описать следующим образом:
1. Планирование запроса: Когда поступает SQL запрос, система анализирует его и строит план выполнения, определяя оптимальный способ доступа к данным и выполнения операций.
2. Обработка запроса: После построения плана выполнения, RedStore начинает выполнение запроса, выполняя операции в соответствии с планом.
3. Интерпретация и оптимизация запроса: RedStore использует современные методы оптимизации запросов, такие как использование индексов, параллельное выполнение запросов, кеширование промежуточных результатов и другие техники, чтобы обеспечить быстрое выполнение запросов.
4. Возврат результатов: По завершении выполнения запроса, RedStore возвращает результаты пользователю, обработанные и подготовленные в соответствии с запросом.
5. Мониторинг и управление: RedStore также предоставляет средства мониторинга выполнения запросов и управления производительностью системы, позволяя администраторам управлять нагрузкой и оптимизировать производительность базы данных.

## Есть ли для вашей СУБД понятие «план запросов»? Если да, объясните, как работает данный этап.
Да, в субд RedStore есть понятие "план запросов" (query plan). План запросов представляет собой оптимизированный план выполнения запроса, который определяет порядок выполнения различных операций, таких как выборка данных, объединение таблиц, сортировка и т. д.

План запросов создается оптимизатором запросов на основе структуры таблиц, индексов, статистики данных и других параметров. Оптимизатор выбирает наиболее эффективный способ выполнения запроса, чтобы минимизировать время выполнения и ресурсы сервера.

После создания плана запросов он используется для выполнения самого запроса. Поэтому важно, чтобы план запросов был оптимизирован и эффективен, чтобы сэкономить время и ресурсы при выполнении запроса.

Таким образом, план запросов играет ключевую роль в оптимизации производительности запросов в субд RedStore.

## Поддерживаются ли транзакции в вашей СУБД? Если да, то расскажите о нем. Если нет, то существует ли альтернатива?
Да, в RedStore поддерживаются транзакции. Транзакции в базе данных представляют собой логически связанное и атомарное (неделимое) выполнение серии операций базы данных. Это означает, что транзакции либо выполняются полностью, либо не выполняются вообще, что помогает обеспечить целостность данных.

В RedStore транзакции поддерживают ACID-свойства, которые включают в себя:

1. Атомарность (Atomicity) — транзакция либо выполнена полностью, либо нет.
2. Согласованность (Consistency) — данные остаются в согласованном состоянии до и после транзакции.
3. Изолированность (Isolation) — транзакции работают независимо друг от друга, изолированно, чтобы избежать конфликтов.
4. Устойчивость (Durability) — изменения, сделанные в рамках транзакции, сохраняются даже в случае сбоя системы.

Таким образом, использование транзакций в RedStore помогает обеспечить сохранность данных и целостность базы данных.

Если в RedStore нет возможности использовать транзакции, альтернативой может быть ручное управление транзакциями при помощи контроля над коммитами и откатами изменений. В этом случае разработчику придется самостоятельно обеспечивать ACID-свойства и управлять выполнением и откатом изменений.

## Какие методы восстановления поддерживаются в вашей СУБД. Расскажите о них.
СУБД REdStore поддерживает следующие методы восстановления данных:
1. Сделки ACID: REdStore обеспечивает поддержку транзакций ACID (атомарности, согласованности, изолированности и долговечности), что обеспечивает надежное восстановление данных в случае сбоев или ошибок.
2. Резервное копирование: REdStore позволяет создавать и восстанавливать резервные копии данных, что позволяет быстро восстанавливать информацию в случае ее утери или повреждения.
3. Журналирование: REdStore записывает все изменения данных в журнал транзакций, что обеспечивает возможность восстановления информации до момента сбоя или ошибки.
4. Репликация данных: REdStore поддерживает репликацию данных, что позволяет создавать резервные копии данных на отдельных узлах или серверах для обеспечения отказоустойчивости и возможности быстрого восстановления.
5. Фрагментация данных: REdStore поддерживает фрагментацию данных, при которой данные разделяются на более мелкие части, что позволяет упростить процесс восстановления при сбоях и снизить вероятность потери всех данных.

## Расскажите про шардинг в вашей конкретной СУБД. Какие типы используются? Принцип работы.
Шардинг в СУБД RedStore используется для горизонтального масштабирования данных путем разделения базы данных на несколько частей, называемых шардами. Каждый шард содержит часть данных и обрабатывает запросы для этой части данных.

RedStore поддерживает два основных типа шардинга: по диапазону ключей и по хэшу ключа. 

При шардинге по диапазону ключей данные разделяются на шарды на основе значений ключей. Например, можно разделить данные по временному интервалу или по географическому региону.

При шардинге по хэшу ключа данные обрабатываются на основе хеширования значений ключей. Это позволяет равномерно распределить данные между шардами и уменьшить количество запросов к каждому шарду.

Принцип работы шардинга в RedStore заключается в том, что каждый запрос отправляется на координатор, который определяет какому шарду он должен быть направлен. Затем запрос передается выбранному шарду для выполнения операции над данными. Координатор также управляет соединением с шардами и обеспечивает целостность данных в процессе выполнения запросов.

Шардинг в RedStore позволяет увеличить производительность и масштабируемость базы данных, распределяя нагрузку на несколько серверов. Однако необходимо учитывать особенности работы с шардированными данными, такие как согласованность данных и балансировка нагрузки между шардами.

## Возможно ли применить термины Data Mining, Data Warehousing и OLAP в вашей СУБД?
Да, возможно применить термины Data Mining, Data Warehousing и OLAP в СУБД RedStore. 

Data Mining (горное дело данных) - это процесс извлечения полезной информации из больших объемов данных, чтобы выявить скрытые закономерности и взаимосвязи. В RedStore можно использовать различные инструменты и методы для проведения анализа данных и выявления интересующих вас паттернов.

Data Warehousing (хранилище данных) - это процесс хранения и управления большими объемами данных для проведения аналитических и отчетных операций. В RedStore можно создать и использовать хранилище данных для хранения и организации информации для последующего анализа.

OLAP (онлайн-аналитическая обработка) - это технология анализа данных, позволяющая проводить многомерный анализ данных и строить отчеты с использованием множества измерений. В RedStore можно использовать OLAP для проведения анализа данных и создания отчетов на основе многомерных данных.

## Какие методы защиты поддерживаются вашей СУБД? Шифрование трафика, модели авторизации и т.п.
СУБД RedStore поддерживает следующие методы защиты:
1. Шифрование трафика - RedStore поддерживает SSL/TLS протоколы для защиты передаваемой информации между клиентом и сервером.
2. Модели авторизации - RedStore поддерживает различные модели авторизации, включая RBAC (Role-Based Access Control) и ABAC (Attribute-Based Access Control), которые позволяют управлять доступом пользователей к данным и операциям.
3. Аудит доступа - RedStore предоставляет возможность вести журналы аудита доступа, чтобы отслеживать кто, когда и что делал в базе данных.
4. Защита от SQL-инъекций - RedStore предоставляет механизмы для защиты от атак SQL-инъекций, например, подготавливаемые запросы.
5. Шифрование данных - RedStore предоставляет возможность шифровать данные на уровне столбцов или целых таблиц для дополнительной защиты информации.
6. Механизмы аутентификации - RedStore поддерживает различные методы аутентификации, такие как использование логина/пароля, сертификатов, интеграция с LDAP и т.д.

## Какие сообщества развивают данную СУБД? Кто в проекте имеет права на коммит и создание дистрибутива версий? Расскажите об этих людей и/или компаниях.
СУБД RedStore развивается сообществом разработчиков, которые активно работают над улучшением и расширением функционала этой системы. В сообществе могут участвовать как индивидуальные разработчики, так и компании, заинтересованные в развитии и поддержке RedStore.

Как правило, участники сообщества имеют равные права на коммит изменений в исходный код проекта и создание дистрибутивов версий. Это делает проект более открытым и доступным для широкого круга пользователей и разработчиков.

В сообществе могут быть как профессионалы с большим опытом работы с СУБД, так и начинающие разработчики, желающие получить новые знания и опыт в этой области. Каждый участник сообщества вносит свой вклад в развитие проекта, и все они равноценны в правах и обязанностях.

Таким образом, сообщество разработчиков RedStore - это дружественное и открытое сообщество, где каждый может найти для себя место и внести свой вклад в развитие этой СУБД.

## Создайте свои собственные данные для демонстрации работы СУБД. 
```sql
@prefix foaf:  <http://xmlns.com/foaf/0.1/> .

_:a  foaf:name   "Johnny Lee Outlaw" .
_:a  foaf:mbox   <mailto:jlow@example.com> .
_:b  foaf:name   "Peter Goodguy" .
_:b  foaf:mbox   <mailto:peter@example.org> .
_:c  foaf:mbox   <mailto:carol@example.org> .
```

## Как продолжить самостоятельное изучение языка запросов с помощью демобазы. Если демобазы нет, то создайте ее.
Для продолжения самостоятельного изучения RedStore можно следовать следующим планом:

1. Изучить документацию и учебные материалы: начните с ознакомления с официальным сайтом RedStore, где можно найти документацию, руководства и другие полезные материалы. Также можно обратиться к онлайн-курсам и видеоурокам, которые помогут лучше понять основные принципы работы с RedStore.
2. Практические упражнения: создайте собственный проект или задачу, которую можно решить с помощью RedStore. Попробуйте реализовать его на практике, испытав все особенности и возможности платформы.
3. Участие в сообществе: присоединитесь к сообществу пользователей RedStore, где можно задавать вопросы, обсуждать проблемы и делиться опытом с другими участниками. Это поможет получить дополнительную поддержку и информацию от опытных пользователей.
4. Постоянное обновление знаний: следите за новостями и обновлениями в мире RedStore, чтобы быть в курсе последних тенденций и изменений на платформе. Постоянно пополняйте свои знания и навыки, чтобы быть более компетентным пользователем RedStore.

Настоятельно рекомендуется также проводить регулярные практические занятия с RedStore, чтобы углубить знания и навыки работы с этой платформой.

## Где найти документацию и пройти обучение
https://github.com/njh/redstore?tab=readme-ov-file

## Как быть в курсе происходящего
Следить за новыми коммитами в открытом репозитории

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
