class GardenError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = ""):
        if message:
            super().__init__(message)
        else:
            super().__init__("Unknown plant error")


class WaterError(GardenError):
    def __init__(self, message: str = ""):
        if message:
            super().__init__(message)
        else:
            super().__init__("Unknown water error")


def test_custom_errors() -> None:
    print("=== Garden Custom Errors Demo ===")
    print()
    try:
        print("Testing PlantError...")
        raise PlantError()
    except PlantError as error:
        print(f"Caught PlantError: {error}")
    print()
    try:
        print("Testing WaterError...")
        raise WaterError("Not enough water in the tank!")
    except WaterError as error:
        print(f"Caught WaterError: {error}")
    print()
    print("Testing catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as error:
        print(f"Caught GardenError: {error}")
    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as error:
        print(f"Caught GardenError: {error}")
    print()
    print("All custom error types work correctly!")


test_custom_errors()
