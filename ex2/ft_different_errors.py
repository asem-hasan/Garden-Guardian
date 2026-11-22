def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("adb")
    elif operation_number == 1:
        1 / 0
    elif operation_number == 2:
        open("non_existent_file.txt", "r")
    elif operation_number == 3:
        "abc" + 1
    else:
        return


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    operation_number = 0
    while operation_number <= 4:
        print(f"Testing operation {operation_number}...")
        try:
            garden_operations(operation_number)
        except ValueError as error:
            print(f"Caught ValueError: {error}")
        except ZeroDivisionError as error:
            print(f"Caught ZeroDivisionError: {error}")
        except FileNotFoundError as error:
            print(f"Caught FileNotFoundError: {error}")
        except TypeError as error:
            print(f"Caught TypeError: {error}")
        operation_number += 1
    print("Operation completed successfully")
    print()
    print("All error types tested successfully!")


test_error_types()
