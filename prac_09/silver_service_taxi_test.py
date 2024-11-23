"""CP1404 Prac_09 silver service taxi test."""

from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    civic = SilverServiceTaxi("Civic", 70, 5)
    civic.drive(30)
    limo = SilverServiceTaxi("Limo", 100, 10)
    limo.drive(65)

    print(civic)
    print(f"The fare was: ${civic.get_fare()}")

    print(limo)
    print(f"The fare was: ${limo.get_fare()}")


main()
