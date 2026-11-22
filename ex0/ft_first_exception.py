def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    print()
    try:
        input_temp = "25"
        print(f"Input data is ’{input_temp}’")
        print(f"Temperature is now {input_temperature(input_temp)}°C")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")
    print()
    try:
        input_temp = "abc"
        print(f"Input data is ’{input_temp}’")
        print(f"Temperature is now {input_temperature(input_temp)}°C")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")
    print()
    print("All tests completed - program didn’t crash!")


test_temperature()
