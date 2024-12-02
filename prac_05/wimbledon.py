""""""

FILENAME = "wimbledon.csv"
COUNTRY_COLUMN_INDEX = 1
CHAMPION_COLUM_INDEX = 2


def main():
    records = get_record(FILENAME)
    countries, number_of_companions = record_processor(records)
    show_outcomes(countries, number_of_companions)


def show_outcomes(countries, number_of_companions):
    print("Wimbledon Champions: ")
    for name, count in number_of_companions.items():
        print(f"{name}: {count}")
    print(f"\nThese {len(countries)} countries have a Wimbledon: ")
    print(", ".join(country for country in sorted(countries)))


def record_processor(records):
    number_of_companions = {}
    countries = set()
    for record in records:
        countries.add(record[COUNTRY_COLUMN_INDEX])
        if record[CHAMPION_COLUM_INDEX] in number_of_companions:
            number_of_companions[record[CHAMPION_COLUM_INDEX]] += 1
        else:
            number_of_companions[record[CHAMPION_COLUM_INDEX]] = 1
    return countries, number_of_companions


def get_record(filename):
    records = []
    with open(FILENAME, "r", encoding="utf-8") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


main()
