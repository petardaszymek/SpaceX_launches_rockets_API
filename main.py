"""
Zadanie

https://api.spacexdata.com/v4/launches

https://api.spacexdata.com/v4/rockets


Stwórz skrypt który będzie generował raport startów rakiet korzystając z powyższych API.

Skrypt będzie przyjmował jako argument rok lub/i miesiąc.

Jeśli zostanie podany tylko rok to raport będzie zawierał starty tylko w podanym roku.

Jeśli zostanie podany tylko miesiąc to raport będzie zawierał starty każdego roku w podanym miesiącu.

Jeśli zostanie podany zarówno rok jak i miesiąc to raport będzie zawierał starty w podanym roku w podanym miesiącu.

Raport zostanie wygenrowany w formacie csv.

Raport będzie zawierał dwie kolumny "static_fire_date_utc", "rocket_name".

"static_fire_date_utc" będzie w formacie "2022-04-20T14:12:00+00:00"

Raport będzie posortowany od najnowszej daty.

Rozwiązanie powinno posiadać UnitTesty.

Rozwiązanie powinno mieć zaimplementowaną obsługę błędów.

Rozwiązanie powinno być napisane w sposób generyczny,
umożliwiający reużycie fragmentów kodu oraz jego szybką modyfikację.


Przykład

static_fire_date_utc, rocket_name

2022-04-20T14:12:00+00:00, Falcon 9

2022-04-06T19:13:00+00:00, Falcon 9

2022-01-23T21:22:00+00:00, Falcon 9

"""

from functions import filter_by_date, get_data, generate_report, transform_data, validation
import os


def generate_raport(file_name, output_path=".", year=None, month=None):
    launches = get_data("https://api.spacexdata.com/v4/launches")
    rockets = get_data("https://api.spacexdata.com/v4/rockets")
    df = transform_data(launches, rockets)
    df = filter_by_date(df, year=year, month=month)
    generate_report(df, file_name=file_name, output_path=output_path)
    validation(os.path.join(output_path, f"{file_name}.csv"))


print(generate_raport("csv_2020_4", output_path="C:/Users/User/Desktop", year=2020, month=4))
