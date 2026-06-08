from core.processing import process_data


def main() -> None:
    input_data = "example"
    result = process_data(input_data)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()