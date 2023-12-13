# Generator Raportów Startów Rakiet SpaceX

## Opis

Ten projekt zawiera skrypt do generowania raportów na podstawie danych dotyczących startów rakiet SpaceX.
Skrypt korzysta z funkcji z modułu `src.functions`, aby tworzyć raporty na podstawie dostarczonych parametrów, takich jak data i nazwa pliku CSV.

## Jak Uruchomić w Bash

1. Otwórz terminal i przejdź do katalogu projektu:

    ```bash
    cd sciezka/do/projektu
    ```

2. Uruchom skrypt `main.py`, podając odpowiednie argumenty:

    ```bash
    python main.py --file_name NAZWA_PLIKU --output_path SCIEZKA_WYJSCIOWA --year ROK --month MIESIAC
    ```

    Przykład:

    ```bash
    python main.py --file_name spacex_launches --output_path C:/Users/User/Desktop --year 2020
    ```

## Argumenty

- `--file_name`: Nazwa pliku CSV zawierającego dane o startach rakiet SpaceX.
- `--output_path`: Ścieżka do katalogu wyjściowego (domyślnie bieżący katalog).
- `--year`: Rok dla raportu (opcjonalny).
- `--month`: Miesiąc dla raportu (opcjonalny).
