from mock_vendors import MOCKVENDORS

CUSTOMERS = MOCKVENDORS


def main():
    for cust in CUSTOMERS:
        print(f"Name: {cust.name}; Address: {cust.address}")


if __name__ == "__main__":
    main()
