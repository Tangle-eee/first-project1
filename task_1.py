#     Задание 1
# Строка содержит пять временных значений. Они записаны через запятую:
# '1h 45m,360s,25m,30m 120s,2h 60s'.
# Напиши цикл, который посчитает общее количество минут. Результат сохрани в переменную и выведи на экран. 
#     Используй в решении методы split(), replace() и оператор in.
# Обрати внимание: 
#     временное значение может состоять из одного, двух или трёх единиц времени. 
# Значения расшифровываются так:
#     часы — любое положительное целое число и символ h;
#     минуты — любое положительное целое число и символ m;
#     секунды — положительное целое число кратное 60 и символ s.


time_string = '1h 45m,360s,25m,30m 120s,2h 60s'
# Разбиваю строку по запятым.
time_values = time_string.split(',') 

total_minutes = 0

for item in time_values:
    parts = item.split()
    minutes = 0
    for part in parts:
        if 'h' in part:
            minutes += int(part.replace('h', '')) * 60
        elif 'm' in part:
            minutes += int(part.replace('m', ''))
        elif 's' in part:
            minutes += int(part.replace('s', '')) // 60
    total_minutes += minutes

print(total_minutes)