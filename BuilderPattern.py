class House():
    __roof: str | None
    __number_of_doors: int 
    __number_of_windows: int

    # There are no private attributes in Python, so
    # it is useless to implement an inner bulder.

    def __init__(
            self, roof: str | None = None, number_of_doors: int = 0,
            number_of_windows: int = 0):
        self.__roof = roof
        self.__number_of_doors = number_of_doors
        self.__number_of_windows = number_of_windows
    
    def __str__(self) -> str:
        return f'roof={self.__roof}, number_of_doors={self.__number_of_doors}, number_of_windows={self.__number_of_windows}'


class HouseBuilder():
    __roof: str | None
    __number_of_doors: int
    __number_of_windows: int

    def roof(self, roof: str | None = None) -> 'HouseBuilder':
        self.__roof = roof
        return self

    def number_of_doors(self, number_of_doors: int = 0) -> 'HouseBuilder':
        self.__number_of_doors = number_of_doors
        return self

    def number_of_windows(self, number_of_windows: int = 0) -> 'HouseBuilder':
        self.__number_of_windows = number_of_windows
        return self
    
    def build(self) -> House:
        return House(
            roof=self.__roof,
            number_of_doors=self.__number_of_doors,
            number_of_windows=self.__number_of_windows
        )


class Director():
    def make_gable_roof_house(self, house_builder: HouseBuilder) -> None:
        house_builder.roof('gable').number_of_doors().number_of_windows()


def main() -> None:
    house_builder: HouseBuilder = HouseBuilder()
    house_builder.roof('straight').number_of_doors(2).number_of_windows(7)
    completed_house: House = house_builder.build()
    print(completed_house)


def main_with_director() -> None:
    house_builder: HouseBuilder = HouseBuilder()
    director: Director = Director()
    director.make_gable_roof_house(house_builder)
    completed_house: House = house_builder.build()
    print(completed_house)


main()
main_with_director()
