class GardenError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = ""):
        if message:
            super().__init__(message)
        else:
            super().__init__("Unknown plant error")


def water_plant(plant_name: str) -> str:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: ’{plant_name}’")
    return "[OK]"


def test_watering_system() -> None:
    print("=== Garden Watering System ===")
    print()
    print("Testing valid plants...")
    try:
        print("Opening watering system")
        plant_name = "Tomato"
        print(f"Watering {plant_name}: {water_plant(plant_name)}")
        plant_name = "Lettuce"
        print(f"Watering {plant_name}: {water_plant(plant_name)}")
        plant_name = "Carrots"
        print(f"Watering {plant_name}: {water_plant(plant_name)}")
    except PlantError as error:
        print(f"Caught PlantError: {error}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")
    print()
    print("Testing invalid plants...")
    try:
        print("Opening watering system")
        plant_name = "Tomato"
        print(f"Watering {plant_name}: {water_plant(plant_name)}")
        plant_name = "lettuce"
        print(f"Watering {plant_name}: {water_plant(plant_name)}")
        plant_name = "Carrots"
        print(f"Watering {plant_name}: {water_plant(plant_name)}")
    except PlantError as error:
        print(f"Caught PlantError: {error}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")
    print()
    print("Cleanup always happens, even with errors!")


test_watering_system()
