from datetime import datetime, date, timedelta
from time import sleep
from pytz import timezone

MSK = timezone('Europe/Moscow')

employees = [
    {"id": 1, "name": "Иванов Иван", "status": None, "periods": None},
    {"id": 2, "name": "Петров Петр", "status": None, "periods": None},
]

default_periods = [
    {"start": date(2024, 9, 1), "end": date(2024, 9, 14)},
    {"start": date(2024, 7, 1), "end": date(2024, 7, 14)},
]


def create_periods():
    for employee in employees:
        employee["periods"] = []
        print(f"Создан пустой график отпусков для {employee['name']}")


def notification():
    for employee in employees:
        if employee["status"] is None:
            print(f"{employee['name']} Не заполнил график!")


def set_default_periods():
    for employee in employees:
        if employee["status"] is None:
            employee["periods"] = default_periods
    print("График закрыт")


if __name__ == "__main__":

    while True:
        now = datetime.now(MSK)
        today = now.date()
        current_time = now.time()
        
        if today.month == 11 and today.day == 1 and current_time.hour == 12 and current_time.minute == 0:
            create_periods()
        
        if today.month == 11 and today.day == 8 and current_time.hour == 12 and current_time.minute == 0:
            notification()
        
        if today.month == 11 and today.day == 15 and current_time.hour == 12 and current_time.minute == 0:
            set_default_periods()
        sleep(60)
