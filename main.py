from datetime import date, datetime, timedelta, UTC
from time import sleep

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


def sleep_until_12_msk():
    now = datetime.now(UTC) + timedelta(hours=3)

    if now.hour >= 12:
        target = now.replace(hour=12, minute=0, second=0, microsecond=0) + timedelta(
            days=1
        )
    else:
        target = now.replace(hour=12, minute=0, second=0, microsecond=0)

    sleep_seconds = (target - now).total_seconds()
    print(
        f"Спим до {target.strftime('%d.%m.%Y %H:%M')} по МСК ({sleep_seconds:.1f} секунд)"
    )
    sleep(sleep_seconds)


if __name__ == "__main__":

    while True:
        today = date.today()
        if today.month == 11 and today.day == 1:
            create_periods()

        if today.month == 11 and today.day == 8:
            notification()

        if today.month == 11 and today.day == 15:
            notification()

        sleep_until_12_msk()
