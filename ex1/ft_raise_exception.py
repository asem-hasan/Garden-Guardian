def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    elif temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    return temp


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    print()
    try:
        input_temp = "25"
        print(f"Input data is ’{input_temp}’")
        print(f"Temperature is now {input_temperature(input_temp)}°C")
    except ValueError as error:
        print("Caught input_temperature error: ", end="")
        print(error)
    print()
    try:
        input_temp = "abc"
        print(f"Input data is ’{input_temp}’")
        print(f"Temperature is now {input_temperature(input_temp)}°C")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")
    print()
    try:
        input_temp = "100"
        print(f"Input data is ’{input_temp}’")
        print(f"Temperature is now {input_temperature(input_temp)}°C")
    except ValueError as error:
        print("Caught input_temperature error: ", end="")
        print(error)
    print()
    try:
        input_temp = "-50"
        print(f"Input data is ’{input_temp}’")
        print(f"Temperature is now {input_temperature(input_temp)}°C")
    except ValueError as error:
        print("Caught input_temperature error: ", end="")
        print(error)
    print()
    print("All tests completed - program didn’t crash!")


test_temperature()
