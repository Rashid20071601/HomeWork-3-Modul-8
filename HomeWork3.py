class IncorrectVinNumber(Exception):
    # Исключение для некорректного VIN-номера
    def __init__(self, message):
        # Сохранение сообщения об ошибке
        self.message = message


class IncorrectCarNumbers(Exception):
    # Исключение для некорректных номеров автомобиля
    def __init__(self, message):
        # Сохранение сообщения об ошибке
        self.message = message


class Car:
    def __init__(self, model, vin, numbers):
        # Инициализация основных атрибутов объекта: модели, VIN и номера
        self.model = model
        self.__vin = vin
        self.__numbers = numbers
        # Валидация VIN-номера через приватный метод __is_valid_vin
        self.__is_valid_vin(self.__vin)
        # Валидация номеров через приватный метод __is_valid_numbers
        self.__is_valid_numbers(self.__numbers)

    @staticmethod
    def __is_valid_vin(vin_number):
        """
        Проверка корректности VIN-номера:
        - Должен быть целым числом в пределах диапазона [1000000, 9999999].
        - Если условие не выполняется, вызывается исключение IncorrectVinNumber.
        """
        if isinstance(vin_number, int):  # Проверка типа на целое число
            if not 1000000 <= vin_number <= 9999999:
                # VIN-номер вне диапазона, выброс исключения
                raise IncorrectVinNumber("Неверный диапазон для vin номера")
            else:
                return True  # VIN-номер корректен
        else:
            # Некорректный тип VIN-номера, выброс исключения
            raise IncorrectVinNumber("Некорректный тип vin номер")

    @staticmethod
    def __is_valid_numbers(numbers):
        """
        Проверка корректности номера автомобиля:
        - Должен быть строкой длиной 6 символов.
        - Если условия не выполняются, выбрасывается исключение IncorrectCarNumbers.
        """
        if isinstance(numbers, str):  # Проверка типа на строку
            if len(numbers) == 6:
                return True  # Номер корректен
            else:
                # Неправильная длина номера, выброс исключения
                raise IncorrectCarNumbers("Неверная длина номера")
        else:
            # Некорректный тип данных для номера, выброс исключения
            raise IncorrectCarNumbers("Некорректный тип данных для номеров")


# Пример создания объектов с обработкой исключений
try:
    # Создание объекта Car с корректным VIN и номером
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    # Обработка исключения для VIN-номера
    print(exc.message)
except IncorrectCarNumbers as exc:
    # Обработка исключения для номера
    print(exc.message)
else:
    # Успешное создание объекта
    print(f'{first.model} успешно создан')

try:
    # Создание объекта Car с некорректным VIN (вызывается исключение)
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    # Создание объекта Car с некорректным номером (вызывается исключение)
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
