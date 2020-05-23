# VirtualMachines
Reading CSV and making report:

В файле vms.csv находится выгрузка данных по виртуальным машинам (ВМ) со следующими столбцами:

id - идентификатор ВМ
cpu - количество CPU в ВМ в штуках
ram - количество оперативной памяти в гигабайтах
hdd_type - тип жесткого диска
hdd_capacity - объем жесткого диска

Во файле prices.csv находится выгрузка данных по ценам на вычислительные ресурсы:

type - тип вычислительных ресурсов
price - цена в копейках

В файле volumes.csv находится выгрузка данных по дополнительным жестким дискам:

vm_id - идентификатор ВМ
hdd_type - тип жесткого диска
hdd_capacity - объем жесткого диска

Python-программа реализует чтение CSV-файлов и систему отчетов. Отчеты выводятся в STDOUT в виде текста.

Отчет most_cheapest выводит n самых дорогих ВМ

Отчет most_expensive выводит n самых дешевых ВМ

Отчет который выводит n самых объемных ВМ по параметру type

Отчет который выводит n ВМ у которых подключено больше всего дополнительных дисков (по количеству) (с учетом типа диска если параметр hdd_type указан)

Отчет который выводит n ВМ у которых подключено больше всего дополнительных дисков (по объему) (с учетом типа диска если параметр hdd_type указан)
