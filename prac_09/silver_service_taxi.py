"""CP1404 Prac_09 silver service taxi."""

from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):

    flag_fall = 4.5

    def __init__(self,name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = fanciness * Taxi.price_per_km

    def __str__(self):
        return f"{super().__str__()} plus flag fall of ${self.flag_fall:.2f}"

    def get_fare(self):
        return super().get_fare() + self.flag_fall