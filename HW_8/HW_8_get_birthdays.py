from datetime import datetime, timedelta

users = [
    {"name": "Roman", "birthday": datetime(year=2022, month=12, day=13)},  # ВТ
    {"name": "Anna", "birthday": datetime(year=2022, month=12, day=14)},  # СР
    {"name": "Vasia", "birthday": datetime(year=2022, month=12, day=15)},  # ТЧ
    {"name": "Ilona", "birthday": datetime(year=2022, month=12, day=16)},  # ПТ
    {"name": "Grigoriy", "birthday": datetime(
        year=2022, month=12, day=17)},  # СБ
    {"name": "Alina", "birthday": datetime(year=2022, month=12, day=18)},  # НД
    {"name": "Sasha", "birthday": datetime(year=2022, month=12, day=19)},  # ПН
    {"name": "Maksim", "birthday": datetime(
        year=2022, month=12, day=20)},  # ВТ
    {"name": "Vita", "birthday": datetime(year=2022, month=12, day=21)},  # СР
    {"name": "Rodrigo", "birthday": datetime(
        year=2022, month=12, day=22)}  # ЧТ
]


def get_birthdays_per_week(n):

    list_persons_mon = ""
    list_persons_tu = ""
    list_persons_wd = ""
    list_persons_th = ""
    list_persons_fr = ""

    birthday_persons = []
    monday_w = []
    tuesday_w = []
    wednesday_w = []
    thursday_w = []
    friday_w = []
    interval = timedelta(days=+n)
    interval_of_birthday = datetime.now() + interval

    for l in users:
        if l["birthday"] < interval_of_birthday:
            birthday_person = l
            birthday_persons.append(birthday_person)
    for n in birthday_persons:
        if n["birthday"].weekday() == 0:
            monday_w.append(n)
        elif n["birthday"].weekday() == 1:
            tuesday_w.append(n)
        elif n["birthday"].weekday() == 2:
            wednesday_w.append(n)
        elif n["birthday"].weekday() == 3:
            thursday_w.append(n)
        elif n["birthday"].weekday() == 4:
            friday_w.append(n)
        elif n["birthday"].weekday() == 5:
            monday_w.append(n)
        elif n["birthday"].weekday() == 6:
            monday_w.append(n)

    print(f"Seturday: ")
    print(f"Monday: ")
    for dm in monday_w:
        mon_day = dm.get("name")
        list_persons_mon += mon_day + ", "
    print(f"Monday: {list_persons_mon}")
    for dt in tuesday_w:
        tu_day = dt.get("name")
        list_persons_tu += tu_day + ", "
    print(f"Tuesday: {list_persons_tu}")
    for dw in wednesday_w:
        wed_day = dw.get("name")
        list_persons_wd += wed_day + ", "
    print(f"Wednesday: {list_persons_wd}")
    for dth in thursday_w:
        th_day = dth.get("name")
        list_persons_th += th_day + ", "
    print(f"Thursday: {list_persons_th}")
    for df in friday_w:
        fr_day = df.get("name")
        list_persons_fr += fr_day + ", "
    print(f"Friday: {list_persons_fr}")


get_birthdays_per_week(6)
